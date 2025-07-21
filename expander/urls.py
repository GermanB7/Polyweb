from django.urls import path
from . import views

app_name = 'expander'

urlpatterns = [
    path('', views.expand_form, name='form'),
    # más adelante podremos añadir /api/expand/ etc.
]
