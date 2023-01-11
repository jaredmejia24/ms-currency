from rest_framework.views import APIView, Response

from ..models import Track_Fee
from ..serializer import Currency_Serializer, Track_Fee_Serializer

from ..helpers import check_base_and_quote, calc_conversion_rate, calc_fee_cost

import datetime


class ChangeCurrencyView(APIView):

    def post(self, request):

        base = request.data['base'].upper()
        quote = request.data['quote'].upper()
        money_request = request.data['money_request']

        if money_request <= 0:
            return Response({"status": "error", "message": "money_request needs to be a number greater than 0"})

        currency_dict = check_base_and_quote(base=base, quote=quote)

        quote = Currency_Serializer(currency_dict['quote'])
        base = Currency_Serializer(currency_dict["base"])

        conversion_rate = calc_conversion_rate(
            base_data=base.data, quote_data=quote.data)

        quote_request = conversion_rate*money_request

        currency_dict['base'].quantity += money_request
        currency_dict['quote'].quantity -= quote_request

        if currency_dict['quote'].quantity <= 0:
            return Response({"status": "error", "message": "Not enough money to fulfill request"})

        currency_dict['base'].save()
        currency_dict['quote'].save()

        fee_cost = calc_fee_cost(base_data=base.data, quote_data=quote.data)
        fee_amount = base.data['exchange'] * money_request * fee_cost
        formatted_fee_amount = float("{:4f}".format(fee_amount))

        Track_Fee.objects.create(
            fee_amount=formatted_fee_amount,
            date_transaction=datetime.datetime.now(),
            money_request=money_request,
            base_currency=currency_dict['base'],
            quote_currency=currency_dict['quote']
        )

        quote = Currency_Serializer(currency_dict['quote'])
        base = Currency_Serializer(currency_dict["base"])

        return Response({'status': "success",
                         'date_transaction': datetime.datetime.now(),
                         'money_request': money_request,
                         'base_currency': base.data['name'],
                         'base_new_quantity': base.data['quantity'],
                         'quote_currency': quote.data['name'],
                         'quote_new_quantity': quote.data['quantity'],
                         'fee_amount': formatted_fee_amount,
                         'conversion_rate': conversion_rate
                         })
