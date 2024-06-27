from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from authentication.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import MyTokenObtainPairSerializer, RegisterSerializer, ProfileSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.conf import settings
from django.contrib.auth import get_user_model

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

@api_view(['POST'])
def verify_token(request):
    token = request.data.get('token')
    print(type(token))
    if token:
        try:
            token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = token_backend.decode(str(token), verify=False)
            email = valid_data['email']

            User = get_user_model()
            user = User.objects.get(email=email)
            if user:
                return JsonResponse({'role': user.role}, status=200)
            return JsonResponse({'message': 'User not found'}, status=404)
        except InvalidToken:
            return JsonResponse({'message': 'Invalid token'}, status=401)
        except TokenError as e:
            return JsonResponse({'Error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=400)

    else:
        return JsonResponse({'message': 'Token is required'}, status=400)    
