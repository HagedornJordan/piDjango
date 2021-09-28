from time import time
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.serializers import UserSerializer, GroupSerializer
from .blink import blinkTest


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class OpenDoor(APIView) :
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        print(request.user)
        print(request)
        #print(request.auth)
        print('here')
        return Response("h")

class Blink(APIView) : 
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        pin = request.GET.get('pin', None)
        blinks = request.GET.get('blinks', None)
        timeBetween = request.GET.get('pause', None)
        blinkTest(pin, blinks, timeBetween)
        return Response ("just blinked!")

