from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            if serializer.is_valid():
                return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer