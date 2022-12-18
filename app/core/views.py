from django.shortcuts import render
from rest_framework.views import APIView, Response

class TestView(APIView):
    
    def get(self,request):
        return Response({"status": "success"})
