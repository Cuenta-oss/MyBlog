from django.urls import path
from appServices import views

urlpatterns = [
    path('', views.services, name='services'),
]
