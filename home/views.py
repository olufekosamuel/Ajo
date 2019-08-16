from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class GroupListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = AjoGroup.objects.filter(is_searchable=1)
    serializer_class = GroupSerializer


class GroupMemberListView(generics.ListCreateAPIView):
    serializer_class = MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return AjoMembers.objects.filter(group__id=self.kwargs['id'])

class IdGeneratorView(generics.ListCreateAPIView):
    queryset = AjoGenerator.objects.all()
    serializer_class = GeneratorSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,request):
        user = request.data.get("user", "")
        group = request.data.get("group", "")
        data = AjoGroup.objects.get(id=group)
        user = CustomUser.objects.get(id=user)

        if request.user != data.admin:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            #check if admin is creating a new id for a user with a unique id already
            try:
                AjoGenerator.objects.get(group=data,user=user)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except AjoGenerator.DoesNotExist:
                AjoGenerator.objects.create(group=data,user=user)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET'])
def IdAccept(request,id):
    permission_classes = (permissions.IsAuthenticated,)
    #checks if a user has a unique id or not
    try:
        uid = AjoGenerator.objects.get(Uid=id)
        #check if user is already in the group so as to avoid multiple of same group for a user
        try:
            AjoMembers.objects.get(member=uid.user,group=uid.group)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        except AjoMembers.DoesNotExist:
            AjoMembers.objects.create(member=uid.user,group=uid.group,savings=0)
            return Response(status=status.HTTP_201_CREATED)
    except AjoGenerator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response({'message':'Passed'})



