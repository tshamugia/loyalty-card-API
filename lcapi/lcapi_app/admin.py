from django.contrib import admin
from .models import Lcapi, Organization
# Register your models here.


class LcapiAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'balance', 'time_create', 'time_update')


admin.site.register(Lcapi, LcapiAdmin)
admin.site.register(Organization)
