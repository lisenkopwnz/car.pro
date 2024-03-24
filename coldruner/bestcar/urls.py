from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('bus/', views.bus_ride),
    path('companion/', views.trip_companion),
    path('about/', views.about, name='about'),
]
