from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# Create your views here.
from .models import UserInfo, AirlineEvent

from .serializer import UserSerializer
from .serializer import AirlineEventSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging, json
import pandas as pd

def index(request):
    return render(request,'main/index.html')

@api_view(['POST'])
def postUserInfo(request, type):
    try:
        print(request.data)
        events = AirlineEvent.objects.all()
        serializer = AirlineEventSerializer(events, many=True)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)
