from rest_framework import serializers
from .models import Stock, Watchlist
from django.contrib.auth.models import User


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'symbol', 'current_price', 'last_updated']


class WatchlistSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    stock_symbol = serializers.CharField(write_only=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'stock', 'stock_symbol', 'added_at']

    def create(self, validated_data):
        user = self.context['request'].user
        symbol = validated_data.pop('stock_symbol').upper()

        stock, _ = Stock.objects.get_or_create(symbol=symbol)
        return Watchlist.objects.create(user=user, stock=stock)
