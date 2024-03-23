from django.http import HttpResponse
from django.shortcuts import render

def index(request):  # HttpRequest
    return HttpResponse("Страница приложения bestcar.")

def bus(request):
    return HttpResponse("<h1> Автобусные маршруты </h1>")
