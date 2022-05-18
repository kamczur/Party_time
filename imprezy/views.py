from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                form.add_error(None, 'Niepoprawny login lub hasło!')

        context = {
            'form' : form
        }

        return render(request, 'login.html', context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

