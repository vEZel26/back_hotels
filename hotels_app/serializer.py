from rest_framework import serializers
from hotels_app.models import NumberReserved


class NumberReservedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberReserved
        fields = '__all__'