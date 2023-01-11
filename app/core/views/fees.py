from rest_framework.views import APIView, Response

from ..models import Track_Fee
from ..serializer import Track_Fee_Serializer

class FeesView(APIView):
    
    def get(self, request):
        
        fees = Track_Fee.objects.all()
        
        serializer = Track_Fee_Serializer(fees, many=True)
        
        return Response(serializer.data)