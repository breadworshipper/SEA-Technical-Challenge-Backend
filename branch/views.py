from rest_framework.decorators import api_view
from .serializers import BranchSerializer
from django.http import JsonResponse
from .models import Branch

# Create your views here.
@api_view(['POST'])
def branch_post(request):
    try:
        # Deserialize the request data using the serializer
        serializer = BranchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(serializer.data, status=201)
        
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)
    
@api_view(['GET'])
def branch_get(request):
    try:
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)

        return JsonResponse(serializer.data, safe=False, status=200)
    
    except Exception as e:
        return JsonResponse({'Error': str(e)}, status=500)
    