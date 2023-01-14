"""Module Export"""
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializer import LcapiSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Lcapi


class LcapiRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = LcapiSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def get_object(self):
        card_id = self.kwargs.get('pk')
        return get_object_or_404(Lcapi, card_id=card_id)
    
    def get_queryset(self):
        return Lcapi.objects.all() # pylint: disable=maybe-no-member
    
    
class LcapiAllUsersView(generics.ListAPIView):
    queryset = Lcapi.objects.all()
    serializer_class = LcapiSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    