from rest_framework import serializers
from .models import Currency, Track_Fee


class Currency_Serializer(serializers.ModelSerializer):

    name = serializers.CharField(min_length=1, allow_blank=False)
    exchange = serializers.FloatField()
    fee_percentage = serializers.FloatField()
    quantity = serializers.FloatField()

    class Meta:
        model = Currency
        fields = ['id', 'name', 'exchange', 'fee_percentage', 'quantity']


class Track_Fee_Serializer(serializers.ModelSerializer):

    money_request = serializers.FloatField(max_value=1000, min_value=1)
    base_currency = Currency_Serializer(read_only=True)
    quote_currency = Currency_Serializer(read_only=True)

    class Meta:
        model = Track_Fee
        fields = ['id', 'base_currency', 'quote_currency', 'money_request',
                  'fee_amount', 'date_transaction']
