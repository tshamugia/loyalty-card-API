from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account, DbReport, Organization, UserField

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('fullname','phone_number', 'time_create', 'time_update')
    
    def fullname(self, obj):
        return f'{obj.name} {obj.surname}'

class ReportAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'time_created','discount', 'station', 'amount')


fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'price', 'address' )})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(Account, AccountAdmin)
admin.site.register(Organization)
admin.site.register(UserField, UserAdmin)
admin.site.register(DbReport, ReportAdmin)
