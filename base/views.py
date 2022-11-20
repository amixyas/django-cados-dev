from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer



@api_view(['GET'])
def endpoints (request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)



@api_view(['GET'])
def advocate_list (request):
    #data = ['Dennis', 'Tadas', 'Max']
    advocates = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def advocate_detail (request, username):
    data = username
    return Response(data)
