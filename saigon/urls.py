from django.contrib import admin
from django.urls import path
from . import views

app_name='saigon'
urlpatterns = [
    path('', views.add, name='add'),
    path('save/', views.predict, name='predict')
]
