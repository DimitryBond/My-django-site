from django.urls import path
from . import views

urlpatterns = [
    path('', views.skills_home, name='skills_home'),
]
