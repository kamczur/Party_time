from datetime import time, date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import URLValidator, MaxLengthValidator, MinLengthValidator, DecimalValidator


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AddPartyForm(forms.Form):
	party_name = forms.CharField(label="Nazwa imprezy")
	party_date = forms.DateField(label="Data imprezy")
	party_time = forms.TimeField(label="Godzina rozpoczęcia imprezy")
	description = forms.CharField(label="Opis")

class GiftForm(forms.Form):
	gift_name = forms.CharField(label="Nazwa prezentu")
	gift_link = forms.CharField(validators=[URLValidator()], label="link do prezentu")
	comments = forms.CharField(label="komentarz")

class GuestForm(forms.Form):
	guest_name = forms.CharField(label="Imię")
	guest_surname = forms.CharField(label="Nazwisko")
	number_of_adults = forms.IntegerField(label="Liczba osób dorosłych")
	number_of_children = forms.IntegerField(label="Liczba dzieci")
	phone_number = forms.IntegerField(label="Numer telefonu")
	comments = forms.CharField(label="Uwagi")
