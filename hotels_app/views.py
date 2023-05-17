
from hotels_app.models import NumberReserved
from rest_framework import viewsets
from rest_framework.response import Response
from hotels_app.serializer import NumberReservedSerializer

class NumberReservedViewSet(viewsets.ModelViewSet):
    queryset = NumberReserved.objects.all()
    serializer_class = NumberReservedSerializer

class DateReserved(viewsets.ViewSet):
    def get_queryset(self):
        
        return super().get_queryset()
    