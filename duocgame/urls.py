
from django.urls import path
from .views import landing_page, singup, login, shoppingcart, admin_panel, cat_accion, cat_terror, dashboard, checkout, profile_modification, restore_pass, shopping_cart, signup, user_panel, visualizacion


urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('singup/', singup, name='singup'),
    path('login/', login, name='login'),
    path('shoppingcart/', shoppingcart, name='shoppingcart'),
    path("admin-panel/", admin_panel, name="admin_panel"),
    path("categoria/accion", cat_accion, name="cat_accion"),
    path("categoria/terror", cat_terror, name="cat_terror"),
    path("dashboard", dashboard, name="dashboard"),
    path("checkout", checkout, name="checkout"),
    path("login", login, name="login"),
    path("profilemodification", profile_modification,
         name="profile_modification"),
    path("restorepass", restore_pass, name="restore_pass"),
    path("shoppingcart", shoppingcart, name="shopping_cart"),
    path("signup", signup, name="signup"),
    path("user_panel", user_panel, name="user_panel"),
    path("visualizacion", visualizacion, name="visualizacion"),

]

