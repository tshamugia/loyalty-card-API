from django.contrib import admin
from .models import Lcapi, Organization
# Register your models here.


class LcapiAdmin(admin.ModelAdmin):
    list_display = ('fullname','phone_number','balance', 'time_create', 'time_update')
    
    def fullname(self, obj):
        return f'{obj.name} {obj.surname}'


admin.site.register(Lcapi, LcapiAdmin)
admin.site.register(Organization)
