from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    admin_panel,
    cat_accion,
    cat_terror,
    checkout,
    dashboard,
    landing_page,
    login_view,
    profile_modification,
    restore_pass,
    shoppingcart,
    signup,
    user_panel,
    visualizacion,
    wip,
    form_juegos,
    mod_juegos,
    eliminar_juego,
)

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("shoppingcart/", shoppingcart, name="shoppingcart"),
    path("admin-panel/", admin_panel, name="admin_panel"),
    path("categoria/accion", cat_accion, name="cat_accion"),
    path("categoria/terror", cat_terror, name="cat_terror"),
    path("dashboard/", dashboard, name="dashboard"),
    path("checkout/", checkout, name="checkout"),
    path("profilemodification/", profile_modification, name="profile_modification"),
    path("restorepass/", restore_pass, name="restore_pass"),
    path("user-panel/", user_panel, name="user_panel"),
    path("visualizacion/", visualizacion, name="visualizacion"),
    path("categoria/wip", wip, name="wip"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("form_juegos/", form_juegos, name="form_juegos"),
    path("mod_juegos/<int:idgame>/", mod_juegos, name="mod_juegos"),
    path("eliminar_juego/<int:idgame>/", eliminar_juego, name="eliminar_juego")
]

