from django.urls import path

from .views import ConnexionView, RegistrationView

urlpatterns = [
    path('login/', ConnexionView.as_view(), name="login"),
    path('registrer/', RegistrationView.as_view(), name="registrer"),
]
