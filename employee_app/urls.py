from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_all', views.view_all, name='view_all'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('remove/<int:emp_id>', views.remove, name='remove'),
    path('filter', views.filter, name='filter')
]