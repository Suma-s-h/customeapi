from django.shortcuts import render
from rest_framework.views import APIView
from status.models import Status
from status.serializer import StatusSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,GenericAPIView
from rest_framework import generics,mixins
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
# from rest_framework import CreateModelMixin




# Create your views here.
class StatusAllListView(APIView):
    permission_classes=[]                               
    authentication_classes=[]


    def get(self,request):
        qs=Status.objects.all()
        serializer=StatusSerializer(qs,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        qs=Status.objects.all()
        serialzer=StatusSerializer(qs,many=True)
        return Response(serialzer.data)



# class StatusAllListView(ListAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer


# class AddNewStatusView(CreateAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer


# class OnestatusApiView(RetrieveAPIView):
#     permission_classes=[]
#     authentication_classes=[]
#     queryset=Status.objects.all()
#     serializer_class=StatusSerializer
#     lookup_field='id'



class flightsListCreateApiView(generics.ListAPIView,mixins.CreateModelMixin):
# class FlightsListCreateApiView(generics.ListAPIView,CreateModelMixin):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StatusRetrieveUpdateDestroyAPIView(UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,GenericAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    













