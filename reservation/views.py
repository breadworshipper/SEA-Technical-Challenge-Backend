from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .services import is_valid_request
from .serializer import ReservationSerializers
from .models import Reservation

# Create your views here.
@api_view(['POST'])
def reservation_post(request):
    try:
        if not is_valid_request(request.data):
            return JsonResponse({"message": "Please provide all required fields."}, status=400)
        
        # Deserialize the request data using the serializer
        serializer = ReservationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return JsonResponse(serializer.data, status=201)
        
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)
    
@api_view(['GET'])
def reservation_get(request):
    try:
        reservations = Reservation.objects.filter(user=request.user)
        serializer = ReservationSerializers(reservations, many=True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)
