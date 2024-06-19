from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializers

import json



@api_view(['GET'])
def get_users(request):
    
    if request.method == 'GET':

        users = User.objects.all()

        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)






















# def databaseEmDjango():

#     data = User.objects.get(pk='gabriel_nick')          # OBJETO

#     data = User.objects.filter(user_age='25')           # QUERYSET

#     data = User.objects.exclude(user_age='25')          # QUERYSET

#     data.save()

#     data.delete()