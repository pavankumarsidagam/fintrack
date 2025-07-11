from django.urls import path
from .views import get_categories, add_transaction

urlpatterns = [
    path('categories/', get_categories, name='get-categories'),
    path('addtransaction/', add_transaction, name='add-transaction'),  
]
