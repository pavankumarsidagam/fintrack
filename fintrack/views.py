from django.http import JsonResponse
from .models.category import Category
from .serializers.category_serializer import CategorySerializer

def get_categories(request):
    categories = Category.objects()
    serialized = [CategorySerializer(cat).data() for cat in categories]
    return JsonResponse(serialized, safe=False)

def add_transaction(request):
    # Placeholder for add_transaction logic
    return JsonResponse({"message": "Transaction added successfully"}, status=201)