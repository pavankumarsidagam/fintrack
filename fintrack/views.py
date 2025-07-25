from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from datetime import datetime

from .models.category import Category
from .serializers.category_serializer import CategorySerializer

from .models.transaction import Transaction
import json


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects()
    serialized = [CategorySerializer(cat).data() for cat in categories]
    return Response(serialized)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_transaction(request):
    try:
        username = request.data.get('username')
        trans_type = request.data.get('type')
        date_str = request.data.get('date')
        description = request.data.get('description', '')
        amount = float(request.data.get('amount', 0))

        date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None

        categories_raw = request.data.get('categories', '{}')
        try:
            categories = json.loads(categories_raw)
        except json.JSONDecodeError:
            return Response({"error": "Invalid categories format"}, status=400)

        transaction = Transaction(
            username=username,
            type=trans_type,
            date=date,
            description=description,
            amount=amount,
            categories=categories
        )
        transaction.save()

        return Response({
            "message": "Transaction added successfully",
            "transaction": transaction.to_dict()
        }, status=201)

    except Exception as e:
        print("Error adding transaction:", e)
        return Response({"error": "Something went wrong"}, status=500)