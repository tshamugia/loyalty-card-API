import datetime

from django.db.models import Sum
from rest_framework import serializers

from .models import Account, DbReport, UserField


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserField
        fields = ('id', 'username', 'price', 'address', 'pincode',)


class ReportSerializer(serializers.ModelSerializer):
    daily_amount = serializers.SerializerMethodField('get_daily_amount')
    daily_cube = serializers.SerializerMethodField('get_daily_cube')

    class Meta:
        model = DbReport
        fields = ('daily_amount', 'daily_cube')

    def get_daily_data(self, obj):
        start_date, end_date = get_today_date_range()
        daily_data = DbReport.objects.filter(station=obj.station, time_created__range=(
            start_date, end_date)).aggregate(daily_amount=Sum('amount'), daily_cube=Sum('cube'))
        return daily_data

    def get_daily_amount(self, obj):
        return self.get_daily_data(obj)['daily_amount'] or 0

    def get_daily_cube(self, obj):
        return self.get_daily_data(obj)['daily_cube'] or 0

    # def get_daily_amount(self, obj):
    #     start_date, end_date = get_today_date_range()
    #     amount = DbReport.objects.filter(station=obj.station, time_created__range=(
    #         start_date, end_date)).aggregate(daily_amount=Sum('amount'))
    #     return amount['daily_amount'] or 0

    # def get_daily_cube(self, obj):
    #     start_date, end_date = get_today_date_range()
    #     cube = DbReport.objects.filter(station=obj.station, time_created__range=(
    #         start_date, end_date)).aggregate(daily_cube=Sum('cube'))
    #     return cube['daily_cube'] or 0


class ReportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DbReport
        fields = '__all__'


def get_today_date_range():
    today = datetime.datetime.today()
    start_date = datetime.datetime(
        year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)
    end_date = datetime.datetime(
        year=today.year, month=today.month, day=today.day, hour=23, minute=59, second=59)
    return start_date, end_date
