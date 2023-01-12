from rest_framework import serializers
from .models import Lcapi, Organization

        
class LcapiSerializer(serializers.ModelSerializer):   
    
    class Meta:
        model = Lcapi
        fields = ('__all__')
        depth = 1
        
   