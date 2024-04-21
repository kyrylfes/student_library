from django.shortcuts import render

from web.models import UserProfile


def profile(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})


def materials(request):
    return render(request, 'library.html')


def books(request):
    return render(request, 'profile.html')
