from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login

from .forms import RegistrationForm, CustomUserForm

# Create your views here.

""" Connexion View """


class ConnexionView(LoginView):
    template_name = "user/login.html"
    authentication_form = CustomUserForm


""" Registration view """


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/registration.html', context={
            'form': RegistrationForm,
        })

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(
                request,
                username=username,
                password=password1
            )
            login(request, user)

        return render(request, "user/registration.html", context={
            'form': RegistrationForm,
        })
