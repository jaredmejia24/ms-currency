from rest_framework import serializers
from .models import Currency, Track_Fee


class Currency_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Currency


class Track_Fee_Serializer(serializers.Serializer):
    
    money_request = serializers.FloatField(max_value=1000, min_value=1)
    base = serializers.CharField(max_length=4, allow_blank=False)
    quote = serializers.CharField(max_length=4, allow_blank=False)


    class Meta:
        model = Track_Fee
        fields = ('base', 'quote', 'money_request')

class setup_Serializer(serializers.Serializer):  

    generate = serializers.BooleanField(required=True)

    class Meta:

        fields = ('generate')