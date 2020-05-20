from django.urls import path
from . import views
#from .views import listaGiornalistiView, listaArticoliView
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='index'),
    #path('lista-articoli', listaArticoliView.as_view(),name='lista_articoli'),
    #path('leggi-giornalisti', listaGiornalistiView.as_view(), name='leggi_giornalisti'),
]