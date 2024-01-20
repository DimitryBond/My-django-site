from django.shortcuts import render


def skills_home(request):
    return render(request, 'skills/skills_home.html')
