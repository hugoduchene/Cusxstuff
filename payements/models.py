from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Products

# Create your models here.


class MethodPayement(models.Model):
    method_payement = models.CharField(max_length=255, blank=False)


class CommandWait(models.Model):
    id_command = models.CharField(max_length=600)
    id_user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.IntegerField(null=False)
    address = models.TextField(blank=False)
    tva = models.CharField(blank=True, max_length=500)
    method_payement = models.ForeignKey(MethodPayement, blank=False, on_delete=models.CASCADE)
    products_buy = models.ManyToManyField(Products, blank=False)
    price_command = models.FloatField(null=False)
    date_command = models.DateTimeField(default=timezone.now)


class CommandDone(models.Model):
    id_command = models.ForeignKey(CommandWait, blank=False, null=False, on_delete=models.CASCADE)
