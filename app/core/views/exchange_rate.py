from rest_framework.views import APIView, Response


import datetime

from ..serializer import Currency_Serializer
from ..helpers import check_base_and_quote, calc_conversion_rate, calc_fee_cost


class ExchangeRateView(APIView):

    def get(self, request, *args, **kwargs):

        base = kwargs['base'].upper()
        quote = kwargs['quote'].upper()

        currency_dict = check_base_and_quote(base=base, quote=quote)

        quote = Currency_Serializer(currency_dict['quote'])
        base = Currency_Serializer(currency_dict["base"])

        formatted_fee_cost = calc_fee_cost(
            base_data=base.data, quote_data=quote.data)

        formatted_conversion_rate = calc_conversion_rate(
            base_data=base.data, quote_data=quote.data)

        return Response({'status': 'success',
                         'current_time': datetime.datetime.now(),
                         'base': base.data['name'],
                         "quote": quote.data['name'],
                         'fee_cost': formatted_fee_cost,
                         'conversion_rate': formatted_conversion_rate})
