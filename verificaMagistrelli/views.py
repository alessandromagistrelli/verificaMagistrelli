from django.shortcuts import render,HttpResponse
import datetime
def index(request): 
    menu = ['news']
    context = {
        'menu': menu,
    }
    return render(request, "home.html", context)