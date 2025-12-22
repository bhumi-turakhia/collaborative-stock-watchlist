from django.db import models
from django.contrib.auth.models import User


class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlists')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'stock')

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol}"


class SharedWatchlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_by_me')
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_with_me')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'shared_with')

    def __str__(self):
        return f"{self.owner.username} → {self.shared_with.username}"
