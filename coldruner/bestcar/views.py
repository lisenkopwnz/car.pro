from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):  # HttpRequest
    return HttpResponse("Страница приложения bestcar.")

def bus_ride(request):
    return HttpResponse("<h1> На автобусе </h1>")

def trip_companion(request):
    return HttpResponse("<h1> C попутчиком </h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h>Упс ,что пошло не так</h>")

