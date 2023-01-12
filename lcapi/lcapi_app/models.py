from django.db import models


class Lcapi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    card_id = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    balance = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey('Organization', null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.card_id)} {self.time_create}'


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return f'{str(self.name)}'