from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status': 'OK'})

class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    
    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class CreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
    
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status': 'OK'})

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
