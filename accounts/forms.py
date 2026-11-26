from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    password_2 = forms.CharField(label="Repeat the password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', "first_name", "email"]

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError("Both passwords should match each other.")
        return data["password2"]

