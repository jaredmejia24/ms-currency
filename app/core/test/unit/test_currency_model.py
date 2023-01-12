import pytest

from core.models import Currency


@pytest.mark.django_db
def test_currency_create():

    currency = Currency.objects.create(
        name='EUR',
        exchange=0.94,
        fee_percentage=0.4,
        quantity=1000
    )

    assert currency.id == 1
    assert currency.name == 'EUR'
    assert currency.exchange == 0.94
    assert currency.fee_percentage == 0.4
    assert currency.quantity == 1000
