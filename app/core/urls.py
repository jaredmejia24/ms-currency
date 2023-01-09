from django.urls import path
from .views import currency

urlpatterns = [
    path("currencies", currency.CurrencyView.as_view()),
    path("generate", currency.GenerateView.as_view())
]
