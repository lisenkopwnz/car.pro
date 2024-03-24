from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string

menu = ["С попутчиками", "На автобусе", "Искать", "Опубликовать поездку"]

def index(request):  # HttpRequest
    data = {'title': "Главная страница",
            "menu": menu
            }
    return render(request, 'bestcar/index.html',context=data)

def about(request):
    data = {'title': "О сайте"}
    return render(request, 'bestcar/about.html',data)

def bus_ride(request):
    return HttpResponse("<h1> На автобусе </h1>")

def trip_companion(request):
    return HttpResponse("<h1> C попутчиком </h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h>Упс ,что пошло не так</h>")

