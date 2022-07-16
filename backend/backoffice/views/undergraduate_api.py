from django.shortcuts import render
from rest_framework.response import Response
from ..models import Undergraduate
from rest_framework.views import APIView
from ..serializers import UndergraduateSerializer

class UndergraduateAPI(APIView):
    def get(self, request):
        queryset = Undergraduate.objects.all()
        print(queryset)
        serializer = UndergraduateSerializer(queryset, many=True)
        return Response(serializer.data)