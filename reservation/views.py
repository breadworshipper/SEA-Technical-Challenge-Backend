from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .services import is_valid_request
from .serializer import ReservationSerializers

# Create your views here.
@api_view(['POST'])
def reservation_post(request):
    try:
        if not is_valid_request(request.data):
            return JsonResponse({"message": "Please provide all required fields."}, status=400)
        
        # Deserialize the request data using the serializer
        serializer = ReservationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(serializer.data, status=201)
        
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)
