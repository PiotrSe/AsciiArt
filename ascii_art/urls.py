from django.urls import path, include
import ascii_art.views

from . import views
path('',ascii_art.views.menu)
