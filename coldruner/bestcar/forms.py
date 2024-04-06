from django.forms import forms
from bestcar.models import *


class Choosing_a_trip(forms.Form):
    name = forms.CharField()
    departure = forms.CharField()
    arrival = forms.CharField()






