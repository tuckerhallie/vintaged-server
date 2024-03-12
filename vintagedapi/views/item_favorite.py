from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from vintagedapi.models import ItemFavorite, Item, User
from vintagedapi.views.item import ItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class ItemFavoriteView(ViewSet):
    def create(self, request):
        user = User.objects.get(uid=request.data["uid"])
        item_id = request.data.get("itemId")

        try:
            item = Item.objects.get(pk=item_id)
            item_favorite, created = ItemFavorite.objects.get_or_create(user=user, item=item)

            if created:
                serializer = ItemFavoriteSerializer(item_favorite)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Item is already favorited"}, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({"error": "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
            user = User.objects.get(uid=request.META.get('HTTP_AUTHORIZATION'))
            item_favorite = ItemFavorite.objects.get(
                item=item,
                user=user
            )
            item_favorite.delete()
            return Response({'message': 'item favorite deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
            item_favorites = ItemFavorite.objects.all()
            serializer = ItemFavoriteSerializer(item_favorites, many=True)
            return Response(serializer.data)
        
    @action(detail=False, methods=['get'], url_path='user-favorites')
    def user_favorites(self, request):
        uid = request.query_params.get('uid')
        if not uid:
            return Response({'error': 'UID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, uid=uid)
        item_favorites = ItemFavorite.objects.filter(user=user)
        serializer = ItemFavoriteSerializer(item_favorites, many=True)
        return Response(serializer.data)

class ItemFavoriteSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    
    class Meta:
        model = ItemFavorite
        fields = ('id', 'user', 'item')
