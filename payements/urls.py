from django.urls import path

from .views import SuccesPayements, FailedPayement

urlpatterns = [
    path('success/', SuccesPayements.as_view(), name="succespayement"),
    path('cancel/', FailedPayement.as_view(), name="failedpayement")
]
