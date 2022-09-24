from django.urls import path
from appStore import views

urlpatterns = [
    path('', views.store, name='store'),
]