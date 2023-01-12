import pytest

from core.models import Track_Fee, Currency


@pytest.mark.django_db
def test_track_fee_create():

    eur_currency = Currency.objects.create(
        name='EUR',
        exchange=0.94,
        fee_percentage=0.4,
        quantity=1000
    )

    usd_currency = Currency.objects.create(
        name='USD',
        exchange=1,
        fee_percentage=0.04,
        quantity=1000
    )

    track_fee = Track_Fee.objects.create(
        fee_amount=0.2,
        money_request=10,
        date_transaction="2023-01-11T00:00:00Z",
        base_currency=eur_currency,
        quote_currency=usd_currency
    )

    assert track_fee.id == 1
    assert track_fee.fee_amount == 0.2
    assert track_fee.money_request == 10
    assert track_fee.date_transaction == "2023-01-11T00:00:00Z"
    assert track_fee.base_currency.name == 'EUR'
    assert track_fee.quote_currency.name == 'USD'
