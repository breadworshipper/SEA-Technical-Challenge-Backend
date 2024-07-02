from .models import Branch, Services
from rest_framework import serializers

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

    def validate(self, data):
        open_time = data.get('open_time')
        close_time = data.get('close_time')

        if open_time and close_time and open_time >= close_time:
            raise serializers.ValidationError("Open time must be less than close time")

        return data
    
    def create(self, validated_data):
        return Branch.objects.create(**validated_data)

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'