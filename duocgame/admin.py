from django.contrib import admin
from .models import UserProfile, Category, Game, Order, OrderItem, Review
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Game)  
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
