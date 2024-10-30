from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('all_emp',all_emp,name='all_emp'),
    path('add_emp',add_emp,name='add_emp'),
    path('remove_emp', remove_emp,name='remove_emp'),
    path('filter_emp',filter_emp,name='filter_emp'),
]

