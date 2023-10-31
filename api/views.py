from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.authtoken.models import Token
from api.serializers import CustomUserSerializer, DeviceSerializer, FlowRateSerializer, LocationSerializer, TemperatureHumidityRecordSerializer
from device.models import Device
from flowrate.models import FlowRate
from location.models import Location
from temperature_recording.models import TemperatureHumidityRecord
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from registration.models import CustomUser
import logging
logger = logging.getLogger(__name__)



class CustomUserListView(APIView):
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    # @method_decorator(csrf_exempt)
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomUserDetailView(APIView):
    def get(self, request, id, format=None):
        user = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        user = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        user = CustomUser.objects.get(id=id)
        user.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)
    


class CustomUserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        logger.debug(f'Username: {username}, Password: {password}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TemperatureListView(APIView):
    serializer_class = TemperatureHumidityRecordSerializer
    def get_queryset(self):
        return TemperatureHumidityRecord.objects.all()
    def get(self, request):
        temperatures = self.get_queryset()
        serializer = TemperatureHumidityRecordSerializer(temperatures, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TemperatureHumidityRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TemperatureDetailView(APIView):
    serializer_class = TemperatureHumidityRecordSerializer
    def get_queryset(self):
        return TemperatureHumidityRecord.objects.all()
    def get_object(self, id):
        try:
            return self.get_queryset().get(id=id)
        except TemperatureHumidityRecord.DoesNotExist:
            raise Http404("Temperature not found")
    def get(self, request, id):
        temperature = self.get_object(id)
        serializer = TemperatureHumidityRecordSerializer(temperature)
        return Response(serializer.data)
    def put(self, request, id):
        temperature = self.get_object(id)
        serializer = TemperatureHumidityRecordSerializer(temperature, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        temperature = self.get_object(id)
        temperature.delete()
        return Response("Temperature deleted", status=status.HTTP_204_NO_CONTENT)


class LocationListCreateView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LocationDetailView(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeviceListAPIView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer= DeviceSerializer(devices, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer= DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DeviceDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            device = Device.objects.get(id=id)
            serializer = DeviceSerializer(device)
            return Response(serializer.data)
        except Device.DoesNotExist:
            return Response("Device not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, id, format=None):
        try:
            device = Device.objects.get(id=id)
            serializer = DeviceSerializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Device.DoesNotExist:
            return Response("Device not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, id, format=None):
        try:
            device = Device.objects.get(id=id)
            device.delete()
            return Response("Device successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except Device.DoesNotExist:
            return Response("Device not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class FlowrateListAPIView(APIView):
    def get(self, request):
        flows = FlowRate.objects.all()
        serializer= FlowRateSerializer(flows, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer= FlowRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class FlowrateDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            flow = FlowRate.objects.get(id=id)
            serializer = FlowRateSerializer(flow)
            return Response(serializer.data)
        except FlowRate.DoesNotExist:
            return Response("FlowRate not found", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)