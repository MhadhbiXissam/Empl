from django.contrib import admin
from django.urls import path
from .views import get_all_employe , update_employee , delete_employees , add_new_employees

urlpatterns = [
    path('api/all', get_all_employe , name='get_all_employe'),
    path('api/update', update_employee , name='update_employee'),
    path('api/delete', delete_employees , name='delete_employees'),
    path('api/add', add_new_employees , name='add_new_employees'),
]

