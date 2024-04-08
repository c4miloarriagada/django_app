
from django.urls import path
from .views import landing_page, index_form


urlpatterns = [
    path('landing', landing_page, name='landing_page'),
    path('landing/form', index_form, name='index_form')
]