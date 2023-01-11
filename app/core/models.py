from django.db import models

# Create your models here.


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=4)
    exchange = models.FloatField()
    fee_percentage = models.FloatField()
    quantity = models.FloatField()

    def __str__(self):
        return super().__str__()


class Track_Fee(models.Model):
    id = models.AutoField(primary_key=True)
    fee_amount = models.FloatField()
    money_request = models.FloatField()
    date_transaction = models.DateTimeField(max_length=45)
    base_currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, related_name='base')
    quote_currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, related_name='quote')

    def __str__(self):
        return super().__str__()

class Is_generated(models.Model):
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return super().__str__()