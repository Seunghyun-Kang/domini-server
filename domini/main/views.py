from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django_pandas.io import read_frame
from functools import reduce
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

@api_view(['PUT'])
def postUserInfo(request, type):
    checkCardList = ['card_samsung','card_shinhan','card_kb','card_bc','card_hyundai','card_nh','card_lotte','card_woori']
    checkMCList = ['mc_skt','mc_kt','mc_lgu','mc_vip']
    checkPayList = ['pay_kakao','pay_naver','pay_payco','pay_smile']
    indexListNotMatch = set()
    indexListMatch = []

    try:
        events = AirlineEvent.objects.all()
        info = json.loads(request.body)
        event_df = read_frame(events)
        
        for i in range(len(event_df.airline)-1):
            indexListMatch.append(event_df['id'].values[i])
            for column in checkCardList:
                if event_df[column].values[i] == 'Y' and info['pay_info'][column] == 'N':
                    indexListNotMatch.add(event_df['id'].values[i])
            for column in checkMCList:
                if event_df[column].values[i] == 'Y' and info['pay_info'][column] == 'N':
                    indexListNotMatch.add(event_df['id'].values[i])
            for column in checkPayList:
                if event_df[column].values[i] == 'Y' and info['pay_info'][column] == 'N':     
                    indexListNotMatch.add(event_df['id'].values[i])

        print(f"IGNORE SET :{indexListNotMatch}")
        for id in indexListNotMatch:
            indexListMatch.remove(id)
            event_df.drop(event_df.loc[event_df['id'] == id].index, inplace= True)
        filter_event = AirlineEvent.objects.filter(id__in=indexListMatch)
        serializer = AirlineEventSerializer(filter_event, many=True)
        return Response(serializer.data)
        
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
