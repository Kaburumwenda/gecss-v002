from django.shortcuts import render
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.db.models import Avg, Count, Q, F
from datetime import datetime
from django.utils import timezone
# Create your views here.

##### AGENTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaAgentList(request):
    user = request.user
    data = MpesaPayment.objects.filter(billRefNumber=user).order_by('-id')[:25]
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)

### TOTALS COUNTS
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaAgentStatic(request):
    agent = request.user
    today_date = datetime.now().strftime('%d')
    month_date = datetime.now().strftime('%m')
    year_date = datetime.now().strftime('%y')
    today = 0
    month = 0
    year = 0
    total = 0
    today_sum = 0
    month_sum = 0
    year_sum = 0
    total_sum = 0
    today_query = MpesaPayment.objects.filter(created__contains=today_date, billRefNumber=agent)
    month_query = MpesaPayment.objects.filter(created__contains=month_date, billRefNumber=agent)
    year_query = MpesaPayment.objects.filter(created__contains=year_date, billRefNumber=agent)
    total_query = MpesaPayment.objects.filter(billRefNumber=agent)

    for ms in today_query:
        today += ms.transAmount
        today_sum = (int(today) * 10) /100
   
    for ms in month_query:
        month += ms.transAmount
        month_sum = (int(month) * 10) / 100
    for ys in year_query:
        year += ys.transAmount
        year_sum = (int(year) * 10) / 100
    for ts in total_query:
        total += ts.transAmount
        total_sum = (int(total) * 10) / 100
    data = [{
       'today':str(today_sum),
       'month':str(month_sum),
       'year': str(year_sum),
       'total':str(total_sum)
    }]
    return Response(data)

#### OFFICE > TRANSACTION

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaList(request):
    data = MpesaPayment.objects.all().order_by('-id')[:50]
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesabyid(request,id):
    data = MpesaPayment.objects.get(id=id)
    serializer = MpesaSerializer(data, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaUpdate(request,id):
    feedback_msg = {}
    query = MpesaPayment.objects.get(id=id)
    serializer = MpesaSerializer(instance=query, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        feedback_msg = { 'error':'false' }
    return Response(feedback_msg)


@api_view(('GET',))
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaSearch(request, cod):
    data = MpesaPayment.objects.filter( Q(transID=cod) | Q(billRefNumber=cod) | Q(firstName=cod) )
    serializer = MpesaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication ])
def mpesaDelete(request, id):
    feedback_msg = {}
    MpesaPayment.objects.get(id=id).delete()
    feedback_msg = { 'error':'false' }
    return Response(feedback_msg)

