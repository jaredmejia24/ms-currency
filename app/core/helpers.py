from rest_framework.exceptions import NotFound

from .models import Currency


def check_base_and_quote(base, quote):

    base = Currency.objects.filter(name=base).first()
    quote = Currency.objects.filter(name=quote).first()

    if (not base):
        raise NotFound("Base Not Found")

    if (not quote):
        raise NotFound("Quote Not Found")

    return {'base': base, "quote": quote}


def calc_conversion_rate(base_data, quote_data):

    conversion_rate = base_data['exchange'] / quote_data['exchange']
    formatted_conversion_rate = float("{:.4f}".format(conversion_rate))

    return formatted_conversion_rate


def calc_fee_cost(base_data, quote_data):

    fee = base_data['fee_percentage'] + quote_data['fee_percentage']
    fee_cost = base_data['exchange'] * fee

    formatted_fee_cost = float("{:.4f}".format(fee_cost))

    return formatted_fee_cost
