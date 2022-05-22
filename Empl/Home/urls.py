from django.contrib import admin
from django.urls import path
from .views import homepage , addnewempl

urlpatterns = [
    path('', homepage , name='homepage'),
    path('add/', addnewempl , name='addnewempl'),

]
