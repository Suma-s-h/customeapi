from django.shortcuts import render
from customeapp.models import FLIGHTS
from customeapp.serializer import FlightsSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage



@csrf_exempt
def FlightAPIView(request,id=0):
    if request.method=='GET':
        flight_data=FLIGHTS.objects.all()
        flight_serializer=FlightsSerializer(flight_data,many=True)
        return JsonResponse(flight_serializer.data,safe=False)
    elif request.method=='POST':
        flight_data=JSONParser().parse(request)
        flight_serializer=FlightsSerializer(data=flight_data)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("Record added successfully",safe=False)
    elif request.method=='PUT':
        new_flight_data=JSONParser().parse(request)
        old_flight_data=FLIGHTS.objects.get(id=new_flight_data['id'])
        flight_serializer=FlightsSerializer(old_flight_data,data=new_flight_data)
        if flight_serializer.is_valid():
            flight_serializer.save()
            return JsonResponse("Record added successfully",safe=False)
    elif request.method=='DELETE':
        flight_data=FLIGHTS.objects.get(id=id)
        flight_data.delete()
        return JsonResponse("Record deleted successfully",safe=False)
        

@csrf_exempt
def SAVEFILE(request):
    files=request.FILES['file']
    file_name=default_storage.save(files.name,files)
    return JsonResponse(file_name,safe=False)
    