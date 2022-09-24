from django.urls import path
from appPost import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('filter_category/<int:id>/', views.filter_category , name='filter_category'),
]
