from django.urls import path
from .views import *
urlpatterns = [
    path('<str:dish>/', app_dis),
]