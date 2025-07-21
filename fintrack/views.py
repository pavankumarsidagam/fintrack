from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

from .models.category import Category
from .serializers.category_serializer import CategorySerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects()
    serialized = [CategorySerializer(cat).data() for cat in categories]
    return Response(serialized)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_transaction(request):
    return Response({"message": "Transaction added successfully"}, status=201)