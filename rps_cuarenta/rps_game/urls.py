from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rock', views.rock, name='rock'),
    path('paper', views.paper, name='paper'),
    path('scissors', views.scissors, name='scissors'),
    path('play', views.play, name='play'),
    path('reset', views.reset, name='reset')
]