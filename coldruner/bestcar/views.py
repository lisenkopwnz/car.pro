from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


from bestcar.models import *

menu = [{'title':'О сайте', 'url_name':'about'},
       {'title':'На автобусе', 'url_name':'bus'},
       {'title':'С попутчиком', 'url_name':'companion'},
       {'title':'Искать', 'url_name':'search'},
       {'title':'Опубликовать поездку', 'url_name':'post'}]

def index(request):  # HttpRequest
    data = {'title': "Главная страница",
            "menu": menu
            }
    return render(request, 'bestcar/index.html',context=data)

def about(request):
    return render(request, 'bestcar/about.html',
                  {'title': 'О сайте',"menu": menu})

def bus_ride(request):
    data = {'title': 'На автобусе'}
    return render(request, 'bestcar/bus_ride.html',context=data)

def trip_companion(request):
    data = {'title': 'С попутчиком'}
    return render(request, 'bestcar/trip_companion.html',context=data)

def search(request):
    data = {'title': 'Искать'}
    return render(request, 'bestcar/search.html',context=data)

def post(request):
    if request.method == 'POST':
       form = Publishing_a_tripForm(request.POST)
       if form.is_valid():
           try:
               Publishing_a_trip.objects.create(**form.cleaned_data)  #form.save()
               return redirect('home')
           except:
               form.add_error(None,'Ошибка добавления поездки')

    else:
        form = Publishing_a_tripForm()
    data = {'form' : form, 'title': 'Опубликовать поездку'}
    return render(request, 'bestcar/post.html',context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h>Упс ,что пошло не так</h>")

