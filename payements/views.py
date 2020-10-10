from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

""" Succes payement """


class SuccesPayements(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payements/success.html')


""" Failed payement """


class FailedPayement(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'payements/cancel.html')
