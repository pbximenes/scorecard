
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analistas', views.analistas, name='analistas'),
    path('metas', views.metas, name='metas'),
    path('avaliacao/<int:userId>', views.avaliacao, name='avaliacao'),

]

