
from django.shortcuts import render
from django.http import HttpResponse
from . import list_of_cities
# Create your views here.
cities = list_of_cities.thousands_of_cities
def index(request):
    return render(request, 'index.html')
