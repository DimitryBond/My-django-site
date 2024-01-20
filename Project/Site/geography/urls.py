from django.urls import path
from . import views

urlpatterns = [
    path('', views.geography_home, name='geography_home'),
]
