from django.shortcuts import render


def geography_home(request):
    return render(request, 'geography/geography_home.html')
