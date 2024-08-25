from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from braces.views import CsrfExemptMixin


class Login(APIView):
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "INVALID CREDENTIALS"}, 
                    status=status.HTTP_401_UNAUTHORIZED)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "INVALID CREDENTIALS"}, status=status.HTTP_401_UNAUTHORIZED) 