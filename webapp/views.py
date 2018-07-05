from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import weather
from . serializers import weatherSerializer
from . serializers import historicalSerializer
from rest_framework import status
import datetime
import random
from dateutil.parser import parse

def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False

@api_view(['GET','POST'])
def weatherList(request):
    if request.method == 'GET':
        weather1 = weather.objects.all()
        # weather1 = weather.objects.filter()
        serializer = historicalSerializer(weather1, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data1 = {'DATE': request.data.get('DATE'), 'TMAX': request.data.get('TMAX'), 'TMIN': request.data.get('TMIN')}
        serializer = weatherSerializer(data=data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
def weatherInfo(request, pk):
    try:
        weather2 = weather.objects.get(pk=pk)
    except weather.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = weatherSerializer(weather2)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        weather2.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def weatherForecast(request, pk):
    date_res = []
    if(is_date(pk)):
        date = datetime.datetime.strptime(pk,"%Y%m%d")
        for i in range(0,7):
            date_res.append(date.strftime('%Y%m%d'))
            date += datetime.timedelta(days=1)
            if(int(date_res[i])>20180215):
                max_temp = round(random.uniform(42, 99),1)
                min_temp = round(random.uniform(8, max_temp),1)
                data1 = {'DATE': date_res[i], 'TMAX': max_temp, 'TMIN': min_temp}
                serializer = weatherSerializer(data=data1)
                if serializer.is_valid():
                    serializer.save()
        try:
            weather3 = weather.objects.filter(pk__in=date_res)
        except weather.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = weatherSerializer(weather3, many=True)
        return Response(serializer.data)
