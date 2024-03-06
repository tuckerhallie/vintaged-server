from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from vintagedapi.models import Item, User, Store, ItemFavorite

class ItemView(ViewSet):
    def retrieve(self, request, pk):
        storeId = request.GET.get("storeId")
        if storeId is not None:
            item = Item.objects.filter(store_id=storeId)
        else:
          item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item, context={'request': request})
        return Response(serializer.data)
    
    def list(self, request):
      items = Item.objects.all()
      serializer = ItemSerializer(items, many=True, context={'request': request})
      return Response(serializer.data)
    
    def create(self, request):
      user = User.objects.get(uid=request.data["user"])
      store = Store.objects.get(pk=request.data["store"])
      
      item = Item.objects.create(
        name=request.data["name"],
        type=request.data["type"],
        color=request.data["color"],
        image=request.data["image"],
        user=user,
        store=store,
      )
      serializer = ItemSerializer(item, context={'request': request})
      return Response(serializer.data)
    
    def update(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.name = request.data["name"]
        item.type = request.data["type"]
        item.color = request.data["color"]
        item.image = request.data["image"]
        store = Store.objects.get(pk=request.data["store"])
        item.store = store
        user = User.objects.get(uid=request.data["user"])
        item.user = user
        item.save()
        
        return Response(None, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    # @action(methods=['post'], detail=False)
    # def create_favorite(self, request):
    #     uid = request.data.get('uid')
    #     item_id = request.data.get('itemId')
    
    # # Fetch or create the user based on UID
    #     user, _ = User.objects.get_or_create(uid=uid)
    
    # # Fetch the item
    #     item = get_object_or_404(Item, id=item_id)
    
    # # Create the favorite
    #     ItemFavorite.objects.get_or_create(user=user, item=item)
    
    #     return Response({'status': 'Item favorited'})
    
    
class ItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = Item
        fields = ('id', 'name', 'type', 'color', 'image', 'user', 'store')
        depth = 1
