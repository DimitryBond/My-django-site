from django.urls import path
from . import views

urlpatterns = [
    path('', views.demand_home, name='demand_home'),
]
