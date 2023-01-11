from django.urls import path

from .views import currency, exchange_rate, generate, change_currency

urlpatterns = [
    path("currencies", currency.CurrencyView.as_view()),
    path("currencies/<int:pk>", currency.CurrencyPkView.as_view()),
    path("generate", generate.GenerateView.as_view()),
    path("check_exchange_rate/<str:base>/<str:quote>",
         exchange_rate.ExchangeRateView.as_view()),
    path("change_currency", change_currency.ChangeCurrencyView.as_view()),
]
