from rest_framework import serializers
from .models import UserInfo, AirlineEvent

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserInfo
        fields = ('__all__')

class AirlineEventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AirlineEvent
        fields = ('__all__')
