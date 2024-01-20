from django.shortcuts import render


def vacancies_home(request):
    return render(request, 'vacancies/vacancies_home.html')
