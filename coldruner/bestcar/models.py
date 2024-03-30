from django.db import models
from django import forms
from django.forms import ModelForm


class Publishing_a_trip(models.Model):
    name = models.CharField(max_length=100,verbose_name="Имя")
    departure = models.CharField(max_length=100,verbose_name="Отправление")
    arrival = models.CharField(max_length=100,verbose_name="Прибытие")
    models_auto = models.CharField(max_length=100,verbose_name="Модель автомобиля")
    date_time = models.DateTimeField(verbose_name="Дата и время")
    seating = models.BigIntegerField(verbose_name="Количество мест")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Publishing_a_tripForm(forms.ModelForm):
    class Meta:
        model = Publishing_a_trip
        fields = ['name', 'departure', 'arrival', 'models_auto', 'date_time', 'seating']
        widgets = { 'date_time': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'})}


def clean_name(self):
    name = self.cleaned_data['name']
    if
