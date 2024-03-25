from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('bus/', views.bus_ride,name='bus'),
    path('companion/', views.trip_companion,name='companion'),
    path('search/', views.search, name='search'),
    path('post', views.post, name='post'),
    path('about/', views.about, name='about'),
]
