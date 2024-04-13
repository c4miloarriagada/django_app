from django.contrib import admin
from .models import UserProfile, Category, Game, Order, OrderItem, Review
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Category)