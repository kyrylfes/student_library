from django.shortcuts import render

from web.models import UserProfile


def profile(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})
