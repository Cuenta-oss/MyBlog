from unicodedata import name
from django.urls import path
from contactApp import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
