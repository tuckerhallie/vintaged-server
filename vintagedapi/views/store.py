from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vintagedapi.models import Store

class StoreView(ViewSet):
    def retrieve(self, request, pk):
      store = Store.objects.get(pk=pk)
      serializer = StoreSerializer(store)
      return Response(serializer.data)
    
    def list(self, request):
      stores = Store.objects.all()
      serializer = StoreSerializer(stores, many=True)
      return Response(serializer.data)
    
    def create(self, request):
      store = Store.objects.create(
        name=request.data["name"],
        address=request.data["address"],
        city=request.data["city"],
        type=request.data["type"],
      )
      serializer = StoreSerializer(store)
      return Response(serializer.data)
    
class StoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    fields = ('id', 'name', 'address', 'city', 'type')
