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


# Requisição por Nick_name
@api_view(['GET', 'PUT'])
def get_by_nick(request, nick):

    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':

        serializer = UserSerializers(user)
        return Response(serializer.data)
    
    if request.method == 'PUT':

        serializer = UserSerializers(user, data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


# CRUD

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

# Acessando dados
    if request.method == 'GET':

        try:
            if request.GET['user']:

                user_nickname = request.GET['user']

                try:
                    user = User.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializers(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Criação de Dados

    if request.method == 'POST':
        
        new_user = request.data

        serializer = UserSerializers(data=new_user)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Modificar Dados

    if request.method == 'PUT':

        nickname = request.data['user_nickname']

        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        #print(request.data)

        serializer = UserSerializers(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)








# def databaseEmDjango():

#     data = User.objects.get(pk='gabriel_nick')          # OBJETO

#     data = User.objects.filter(user_age='25')           # QUERYSET

#     data = User.objects.exclude(user_age='25')          # QUERYSET

#     data.save()

#     data.delete()