from django.urls import path
from . import views

app_name = 'expander'

urlpatterns = [
    path('', views.expand_form, name='form'),
    path('ajax/expand/', views.expand_ajax, name='expand_ajax'),
    # más adelante podremos añadir /api/expand/ etc.
]
