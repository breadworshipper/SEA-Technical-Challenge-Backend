from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from authentication.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import MyTokenObtainPairSerializer, RegisterSerializer, ProfileSerializer

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return JsonResponse(serializer.data)
