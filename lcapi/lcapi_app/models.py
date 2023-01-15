from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from rest_framework.authtoken.models import Token



class Lcapi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=120, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex = r"\b5[0-9]{8}\b")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length=9, blank=True, null=True )
    card_id = models.CharField(max_length=120,  blank=True, null=True)
    balance = models.DecimalField(decimal_places=2, max_digits=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey('Organization', null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return f'{str(self.name)}'
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)