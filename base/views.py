from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from rest_framework.views import APIView

from .models import Advocate
from .serializers import AdvocateSerializer

@api_view(['GET'])
def endpoints (request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)



@api_view(['GET', 'POST'])
def advocate_list (request):
    if request.method == 'GET':
        
        #data = ['Dennis', 'Tadas', 'Max']
        query = request.GET.get('query')

        if query == None:
            query = ''

        print('Query: ',query)
        #http://127.0.0.1:8000/advocates/?query=y
        #advocates = Advocate.objects.all()
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    

    if request.method == 'POST':

        advocates = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
            )
        serializer = AdvocateSerializer(advocates, many=False)

        return Response(serializer.data)



class AdvocateDetail(APIView):
    
    def get(self, request, username):
        advocate = Advocate.objects.get(username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def post(self, request, username):
        advocate = Advocate.objects.get(username=username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = Advocate.objects.get(username=username)
        advocate.delete()
        return Response('user deleted')


""" 
@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail (request, username):

    advocate = Advocate.objects.get(username=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        advocate.delete()
        return Response('user deleted')
 """