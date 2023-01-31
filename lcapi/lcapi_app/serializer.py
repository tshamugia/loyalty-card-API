import datetime

from django.db.models import Sum
from rest_framework import serializers

from .models import Account, DbReport, UserField


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')
        depth = 1
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserField
        fields = ('id', 'username', 'price', 'address')
        

class ReportSerializer(serializers.Serializer):
    daily_amount = serializers.SerializerMethodField('get_daily_amount')
    daily_cube = serializers.SerializerMethodField('get_daily_cube')
    
    class Meta:
        model = DbReport
        fields = ('__all__')


    def get_daily_amount(self, obj):
        station = obj.station
        today = datetime.datetime.today()
        start_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)  # represents 00:00:00
        end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)  # represents 23:59:59
        amount = DbReport.objects.filter(station=station, time_created__range=(start_date, end_date)).aggregate(daily_amount=Sum('amount')) # today's objects
        return amount['daily_amount']

   
    def get_daily_cube(self, obj):
        station = obj.station
        today = datetime.datetime.today()
        start_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)  # represents 00:00:00
        end_date = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)  # represents 23:59:59
        cube = DbReport.objects.filter(station=station, time_created__range=(start_date, end_date)).aggregate(daily_cube=Sum('cube'))  # today's objects
        return cube['daily_cube']


class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbReport
        fields = ('__all__')
