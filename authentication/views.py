from django.shortcuts import render
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authentication import models
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.




@api_view(['POST'])
def delete_user(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def Registration(request):
    if request.method == 'POST':
        account = Registration_serializers(data=request.data)

        data = {}

        if account.is_valid():

            db =account.save()

            data['username'] = db.username
            data['email'] = db.email
            token = Token.objects.get(user=db).key
            data['token'] = token
            
        else:
            return Response(account.errors)
        return Response(data)





