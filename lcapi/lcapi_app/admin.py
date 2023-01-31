

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ExportActionMixin, ImportExportActionModelAdmin
from rangefilter.filters import DateRangeFilter

from .models import Account, DbReport, Organization, UserField

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('fullname','phone_number', 'time_create', 'time_update')
    
    def fullname(self, obj):
        return f'{obj.name} {obj.surname}'

class ReportAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('card_id', 'time_created', 'discount', 'station', 'amount', 'cube')
    list_filter = ('station', ('time_created', DateRangeFilter))



    """
    daily amount and cube should be calculate by day!!! NEED FIX
    """
    # def daily_amount(self, obj):
    #     station = obj.station
    #     today = datetime.datetime.today()
    #     start_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)  # represents 00:00:00
    #     end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)  # represents 23:59:59
    #     amount = DbReport.objects.filter(station=station, time_created__range=(start_date, end_date)).aggregate(daily_amount=Sum('amount'))  # today's objects
    #     return amount['daily_amount']
    
    # def daily_cube(self, obj):
    #     station = obj.station
    #     today = datetime.datetime.today()
    #     start_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)  # represents 00:00:00 
    #     end_date = datetime.datetime(year=today.year, month=today.month, day=today.day , hour=23, minute=59, second=59)  # represents 23:59:59
    #     cube = DbReport.objects.filter(station=station, time_created__range=(start_date, end_date)).aggregate(daily_cube=Sum('cube'))  # today's objects
    #     return cube['daily_cube']

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'price', 'address' )})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(Account, AccountAdmin)
admin.site.register(Organization)
admin.site.register(UserField, UserAdmin)
admin.site.register(DbReport, ReportAdmin)
