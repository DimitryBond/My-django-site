from django.shortcuts import render


def demand_home(request):
    return render(request, 'demand/demand_home.html')
