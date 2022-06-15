from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

from .forms import NewUserForm, AddPartyForm, GiftForm, GuestForm
from .models import Party, Gift, Guest
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def homepage(request):
    """Load the homepage
    :return: Homepage html
    """
    return render(request=request, template_name='homepage.html')


def register_request(request):
    """Register the new app user
    :return: Register Form
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Rejestracja przebiegła pomyślnie")
            return redirect("homepage")
        else:
            messages.error(request, "Rejestracja nie powiodła się. Podano błędne informacje.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    """Login user or inform about wrong credentials
    :return: Login Form
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Jesteś zalogowany jako {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Wprowadzono złą nazwę użytkownika lub hasło.")
        else:
            messages.error(request, "Wprowadzono złą nazwę użytkownika lub hasło.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
    """Logout user
    :return: Homepage
    """
    logout(request)
    messages.info(request, "Wylogowano się poprawnie.")
    return redirect("homepage")


class AddParty(LoginRequiredMixin, View):
    """Allows the logged user to add the party
    :return: Party Form"""

    login_url = "/login"

    def get(self, request):
        form = AddPartyForm()
        return render(request, 'addParty.html', {'form': form})

    def post(self, request):
        form = AddPartyForm(request.POST)
        if form.is_valid():
            party_name = form.cleaned_data['party_name']
            party_date = form.cleaned_data['party_date']
            party_time = form.cleaned_data['party_time']
            description = form.cleaned_data['description']
            user = request.user
            Party.objects.create(party_name=party_name, party_date=party_date, party_time=party_time, description=description, user=user)
            return redirect("party-list")
        else:
            return render(request, 'addParty.html', {'form': form})


class PartiesListView(LoginRequiredMixin, View):
    """displays the list of all parties stored in DB
    :return: Parties html"""
    login_url = "/login"

    def get(self, request):
        parties = Party.objects.all()
        return render(request, "parties.html", context={"parties": parties})


class AddGiftView(View):
    """allows the logged user to add a desirable gift
    :return: Gifts Form
    """

    def get(self, request):
        form = GiftForm()
        return render(request, 'gifts.html', {'form':form})

    def post(self, request):
        form = GiftForm(request.POST)
        if form.is_valid():
            gift_name = form.cleaned_data['gift_name']
            gift_link = form.cleaned_data['gift_link']
            comments = form.cleaned_data['comments']
            Gift.objects.create(gift_name=gift_name, gift_link=gift_link, comments=comments)
            return redirect('gifts-list')
        return render(request, 'gifts.html', {'form': form})


class GiftsListView(View):
    """displays the list of all gifs stored in DB
    :return: Gifts list Html
    """
    def get(self, request):
        gifts = Gift.objects.all().order_by('gift_name')
        return render(request, "giftsList.html", {"gifts": gifts})


class ReserveGiftView(View):
    """allows the user to reserve a gift to buy
    :return: Gifts List html"""
    def get(self, request, gift_id):
        gift = Gift.objects.get(id=gift_id)
        return render(request, "giftsList.html", {"gift": gift})

    def post(self, request, gift_id):
        gift = Gift.objects.get(id=gift_id)
        comment = request.POST.get("comment")
        Gift.objects.create(gift=gift, comment=comment, availability=False)
        gift.save()
        return render(request, "giftsList.html", {"gift": gift})


class GiftReservedView(View):
    """displays last page
    :return: Last Page Html
    """
    def get(self, request, gift_id):
        gift = Gift.objects.get(id=gift_id)
        return render(request, "giftReserved.html", {'gift':gift})


class DeleteGiftView(View):
    """delete gift
    :return: Gifts List Html"""
    def get(self, request, gift_id):
        gift = Gift.objects.get(id=gift_id)
        gift.delete()
        return redirect("gifts-list")


class DeletePartyView(View):
    """delete party
    :return: Party List Html
    """
    def get(self, request, party_id):
        party = Party.objects.get(id=party_id)
        party.delete()
        return redirect("party-list")


class EditPartyView(View):
    """edit party
    :return: Party Form"""
    def get(self, request, party_id):
        party = Party.objects.get(id=party_id)
        data = {'party_name': party.party_name, 'party_date': party.party_date, 'party_time': party.party_time, 'description':party.description}
        form = AddPartyForm(initial=data)
        return render(request, "editParty.html", {"party": party, "form": form})

    def post(self, request, party_id):
        form = AddPartyForm(request.POST)
        if form.is_valid():
            party = Party.objects.get(id=party_id)
            party_name = form.cleaned_data['party_name']
            party_date = form.cleaned_data['party_date']
            party_time = form.cleaned_data['party_time']
            description = form.cleaned_data['description']
            user = request.user
            p = Party(party_name=party_name, party_date=party_date, party_time=party_time, description=description, user=user)
            p.save()
            party.delete()
            return redirect("party-list")

        else:
            return render(request, 'editParty.html', {'form': form})


class PartyDetailsView(View):
    """displays details of party
    :returns: Details Party Html"""
    def get(self, request, party_id):
        party = Party.objects.get(id=party_id)
        return render(request, "detailsParty.html", {'party':party})


class GuestsView(View):
    """alows user to sign up to a party
    :returns: Party Form
    """
    def get(self, request, party_id):
        form = GuestForm()
        party = Party.objects.get(id=party_id)
        return render(request, 'guests.html', {'form':form, 'party':party})

    def post(self, request, party_id):
        party = Party.objects.get(id=party_id)
        form = GuestForm(request.POST)
        if form.is_valid():
            guest_name = form.cleaned_data['guest_name']
            guest_surname = form.cleaned_data['guest_surname']
            number_of_adults = form.cleaned_data['number_of_adults']
            number_of_children = form.cleaned_data['number_of_children']
            phone_number = form.cleaned_data['phone_number']
            comments = form.cleaned_data['comments']

            Guest.objects.create(guest_name=guest_name, guest_surname=guest_surname, number_of_adults=number_of_adults,
                                 number_of_children=number_of_children, phone_number=phone_number, comments=comments, party=party)
            messages.success(request, "Zapisałeś się na imprezę")
            return redirect("last-page")
        else:
            return render(request, 'guests.html', {'form': form})


class LastPageView(View):
    """displays last page
    :return: Last Page Html
    """
    def get(self, request, party_id):
        party = Party.objects.get(id=party_id)
        return render(request, "lastPage.html", {'party':party})









