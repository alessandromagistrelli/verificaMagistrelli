from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

def index(request): 
    api_list = ['lista-articoli','lista-giornalisti']
    context = {
        'api_list': api_list,
    }
    return render(request, "news/home.html", context)

