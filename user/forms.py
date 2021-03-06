from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField
)

""" Manages registration form """


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control input_login', 'placeholder': 'Password'}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control input_login', 'placeholder': 'Confirm password'}
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control input_login', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control input_login', 'placeholder': 'Mail'}),
        }


""" Manages user's forms """


class CustomUserForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'form-control input_login', 'placeholder': 'Username'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input_login', 'placeholder': 'Password', 'autocomplete': 'password'}
        )
    )