from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils.translation import gettext as _


def landing(request):
    return render(request, 'main/landing.html')

def team(request):
    return render(request, 'main/team.html')