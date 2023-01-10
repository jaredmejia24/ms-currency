from rest_framework.views import APIView, Response
from rest_framework.exceptions import NotFound

import datetime

from ..serializer import Currency_Serializer
from ..models import Currency

class ExchangeRateView(APIView):

    def get(self, request, *args, **kwargs):

        base = kwargs['base'].upper()
        quote = kwargs['quote'].upper()

        base = Currency.objects.filter(name=base).first()
        quote = Currency.objects.filter(name=quote).first()

        if (not base):
            raise NotFound("Base Not Found")

        if (not quote):
            raise NotFound("Quote Not Found")

        quote = Currency_Serializer(quote)
        base = Currency_Serializer(base)

        fee = base.data['fee_percentage'] + quote.data['fee_percentage']
        fee_cost = base.data['exchange'] * fee

        formatted_fee_cost = float("{:.4f}".format(fee_cost))

        conversion_rate = base.data['exchange'] / quote.data['exchange']
        formatted_conversion_rate = float("{:.4f}".format(conversion_rate))

        return Response({'status': 'success',
                         'current_time': datetime.datetime.now(),
                         'base': base.data['name'],
                         "quote": quote.data['name'],
                         'fee_cost': formatted_fee_cost,
                         'conversion_rate': formatted_conversion_rate})