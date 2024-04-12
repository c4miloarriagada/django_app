
from django.urls import path
from .views import landing_page, singup, login, shoppingcart


urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('singup/', singup, name='singup'),
    path('login/', login, name='login'),
    path('shoppingcart/', shoppingcart, name='shoppingcart')
]

