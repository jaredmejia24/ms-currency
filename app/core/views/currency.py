from rest_framework.exceptions import NotFound
from rest_framework.views import APIView, Response
from ..models import Currency
from ..serializer import Currency_Serializer


class CurrencyView(APIView):

    def get(self, request):

        currencies = Currency.objects.all()
        serializer = Currency_Serializer(currencies, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = Currency_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CurrencyPkView(APIView):

    def get(self, request, *args, **kwargs):

        pk = kwargs['pk']

        currency = Currency.objects.filter(id=pk).first()

        if (not currency):
            raise NotFound("Currency Not Found")

        serializer = Currency_Serializer(currency)

        return Response(serializer.data)
