from django.shortcuts import render
from rest_framework.decorators import api_view
from .services import is_valid_request
from django.http import JsonResponse
from .serializer import ReviewSerializer
from .models import Review
from django.core.paginator import Paginator

# Create your views here.
@api_view(['POST'])
def review_post(request):
    try:
        if not is_valid_request(request.data):
            return JsonResponse({"message": "Please provide all required fields."}, status=400)
        
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(serializer.data, status=201)
        
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)

@api_view(['GET'])
def review_get(request, page_number):
    try:
        per_page = 5
        reviews = Review.objects.all().order_by('-created_at')

        paginator = Paginator(reviews, per_page)
        page_obj = paginator.get_page(page_number)
        data = [{"name": review.name, "date": review.created_at, "review": review.review, "rating": review.rating} for review in page_obj.object_list]

        payload = {
             "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "total_pages": paginator.num_pages
        },
        "data": data
        }

        return JsonResponse(payload, status=200)
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)