from rest_framework import serializers
from .models import Reservation

class ReservationSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=15)
    type_of_service = serializers.CharField(max_length=100)
    date = serializers.DateField()
    time = serializers.TimeField()

    def create(self, validated_data):
        return Reservation.objects.create(**validated_data)
