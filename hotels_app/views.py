
from hotels_app.models import NumberReserved
from rest_framework import viewsets, status
from rest_framework.response import Response
from hotels_app.serializer import NumberReservedSerializer
from rest_framework.views import APIView
from datetime import datetime,timedelta,date

def get_data_reserved(number):
    list_date = []
    delta = timedelta(days=1)
    while number.date_start_reserved <= number.date_end_reserved:
        list_date.append(number.date_start_reserved.strftime("%m.%d.%Y"))
        number.date_start_reserved += delta
    return list_date

class NumberReservedViewSet(viewsets.ModelViewSet):
    queryset = NumberReserved.objects.all()
    serializer_class = NumberReservedSerializer

class DateReserved(APIView):
    def get(self, request, format=None):
        number_type = self.request.query_params.get('type')
        reserved_numbers = NumberReserved.objects.filter(type=number_type)
        data_reserved = [get_data_reserved(number) for number in reserved_numbers]
        response = [item for sublist in data_reserved for item in sublist]


        return Response(response, status=status.HTTP_200_OK)