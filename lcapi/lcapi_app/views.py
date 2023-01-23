"""Module Export"""

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Account, DbReport, UserField
from .serializer import (AccountSerializer, ReportCreateSerializer,
                         ReportSerializer, UserSerializer)


class AccountRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get_object(self):
        card_id = self.kwargs.get('pk')
        return get_object_or_404(Account, card_id=card_id)
    
    
    def get_queryset(self):
        return Account.objects.all()
   
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
    
    
    def get_object(self):
        username = self.kwargs.get('pk')
        return get_object_or_404(UserField, username=username)
    
    def get_queryset(self):
        return UserField.objects.all()

class ReportGetView(generics.ListAPIView):
    serializer_class = ReportSerializer
    queryset = DbReport.objects.all()[:1]
    
   
class ReportCreateView(generics.CreateAPIView):
    serializer_class = ReportCreateSerializer
    queryset = DbReport.objects.all()
