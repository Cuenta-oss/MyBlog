from django.urls import path
""" from . import views """
from .views import registro_user, log_out, log_in
urlpatterns = [
    path('', registro_user.as_view(), name='auth'),
    path('log_out', log_out, name='log_out'),
    path('log_in', log_in, name='log_in'),
]