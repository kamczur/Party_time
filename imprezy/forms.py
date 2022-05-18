from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='login')
    password = forms.CharField(widget=forms.PasswordInput)