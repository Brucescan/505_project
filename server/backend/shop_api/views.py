from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shop
from .serializers import ShopSerializer
from rest_framework.permissions import AllowAny


class ShopSortedListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        shops = Shop.objects.all().order_by('-rating')  # 直接使用 order_by 进行排序
        serializer = ShopSerializer(shops, many=True)
        return Response({'code': 0, 'data': serializer.data})


class ShopListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response({'code': 0, 'data': serializer.data})


class ShopDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, shop_id, format=None):
        try:
            shop = Shop.objects.get(id=shop_id)
            serializer = ShopSerializer(shop)
            return Response({'code': 0, 'data': serializer.data})
        except Shop.DoesNotExist:
            return Response({'code': 1, 'message': 'Shop not found'}, status=status.HTTP_404_NOT_FOUND)


class ShopSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        queryset = Shop.objects.all()
        name = request.query_params.get('name', None)
        address = request.query_params.get('address', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if address is not None:
            queryset = queryset.filter(address__icontains=address)
        serializer = ShopSerializer(queryset, many=True)
        return Response({'code': 0, 'data': serializer.data})
