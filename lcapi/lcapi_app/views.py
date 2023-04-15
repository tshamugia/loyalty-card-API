"""Module Export"""

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Account, DbReport, UserField
from .serializer import (AccountSerializer, ReportCreateSerializer,
                         ReportSerializer, UserSerializer)


class AccountRetrieveUpdateView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Account.objects.all()
    lookup_field = 'card_id'


class AccountAllUsersView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class UsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return UserField.objects.exclude(username='root')


class GetUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = UserField.objects.all()
    lookup_field = 'username'


class ReportCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ReportCreateSerializer
    queryset = DbReport.objects.all()


class ReportGetView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ReportSerializer

    def get_queryset(self):
        station = self.request.user
        queryset = DbReport.objects.filter(station=station)
        return queryset[:1]
