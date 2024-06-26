from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    review = serializers.CharField(max_length=500)
    rating = serializers.IntegerField()

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
