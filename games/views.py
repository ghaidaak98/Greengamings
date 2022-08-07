from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils.translation import gettext as _


def home(request):
    return render(request, 'games/home.html')

def guess_the_habitat_one(request):
    return render(request, 'games/guess_the_habitat/level_one.html')

def guess_the_habitat_two(request):
    return render(request, 'games/guess_the_habitat/level_two.html')

def guess_the_habitat_three(request):
    return render(request, 'games/guess_the_habitat/level_three.html')