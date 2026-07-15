from rest_framework import serializers
from customeapp.models import FLIGHTS

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FLIGHTS
        fields="__all__"