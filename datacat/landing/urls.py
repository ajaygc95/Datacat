from django.contrib import admin
from .views import home
from django.urls import path,include


urlpatterns = [


    path("",home, name='add-to-cart'),

]
