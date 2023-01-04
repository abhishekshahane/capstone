
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import list_of_cities
from django.urls import reverse

# Create your views here.
cities = list_of_cities.thousands_of_cities
def index(request):
    return render(request, 'index.html', {
        'cities': cities
    })
def loading(request):
    if request.method == 'POST':
        # chosen city for that session
        request.session["city_chosen"] = request.POST["user_city"]
        print(request.session["city_chosen"])
        return render(request, 'snowflake_animation.html')
        # Animations after this
    # fill out the form first!
    return HttpResponseRedirect(reverse('index'))
        