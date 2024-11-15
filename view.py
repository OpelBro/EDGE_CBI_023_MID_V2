from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.utils import timezone

@api_view(['GET', 'PATCH'])
def update_item_quantity(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Return the item details
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        # Decrease the quantity of the item
        decrease_by = request.data.get('quantity', None)
        if decrease_by is None or decrease_by <= 0:
            return Response({'detail': 'Invalid quantity value.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if item.quantity < decrease_by:
            return Response({'detail': 'Not enough stock to decrease.'}, status=status.HTTP_400_BAD_REQUEST)
        
        item.quantity -= decrease_by
        item.last_updated = timezone.now()
        item.save()

        serializer = ItemSerializer(item)
        return Response(serializer.data)
