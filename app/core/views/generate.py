from rest_framework.views import APIView, Response
from ..models import Is_generated
from ..serializer import Currency_Serializer

class GenerateView(APIView):

    def post(self, request):

        is_generated = Is_generated.objects.first()

        if (is_generated):
            return Response({'status': "error", "message": "Currencies already generated"}, status=409)

        currencies = [{"name": "EUR", 'exchange': 0.94, 'fee_percentage': 0.4, 'quantity': 1000},
                      {"name": "USD", 'exchange': 1,
                          'fee_percentage': 0.04, 'quantity': 1000},
                      {"name": "JPY", 'exchange': 131.80,
                          'fee_percentage': 0.7, 'quantity': 1000},
                      {"name": "GBP", 'exchange': 0.83,
                          'fee_percentage': 0.9, 'quantity': 1000},
                      {"name": "CHF", 'exchange': 0.93,
                          'fee_percentage': 0.4, 'quantity': 1000},
                      {"name": "AUD", 'exchange': 1.45,
                          'fee_percentage': 0.2, 'quantity': 1000},
                      {"name": "CAD", 'exchange': 1.34,
                          'fee_percentage': 0.3, 'quantity': 1000},
                      {"name": "NZD", 'exchange': 1.57, 'fee_percentage': 0.6, 'quantity': 1000}]

        serializer = Currency_Serializer(data=currencies, many=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        Is_generated.objects.create()

        return Response({"status": "success", "message": "Currencies succesfully added"})
