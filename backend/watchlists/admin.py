from django.contrib import admin
from .models import Stock, Watchlist, SharedWatchlist

admin.site.register(Stock)
admin.site.register(Watchlist)
admin.site.register(SharedWatchlist)
