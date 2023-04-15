from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class DbReport(models.Model):
    id = models.AutoField(primary_key=True)
    card_id = models.CharField(max_length=120,  blank=True, null=True,)
    discount = models.FloatField(null=False)
    station = models.CharField(max_length=100)
    station_price = models.FloatField()
    amount = models.FloatField()
    cube = models.FloatField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)



class UserField(AbstractUser):
    price = models.FloatField(null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=100, blank=True, null=True)



class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    discount = models.FloatField(null=True)
    
    def __str__(self):
        return f'{str(self.name)}'
    
def default_organization():
    return Organization.objects.get(name='default')
    
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=120, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex = r"\b5[0-9]{8}\b")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length=9, blank=True, null=True )
    card_id = models.CharField(max_length=120,  blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey('Organization', null=True, blank=False, on_delete=models.SET_NULL, default=default_organization)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
