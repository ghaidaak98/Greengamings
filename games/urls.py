"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='games_home'),
    path('guess-the-habitat/level-one', views.guess_the_habitat_one, name='guess_the_habitat_one'),
    path('guess-the-habitat/level-two', views.guess_the_habitat_two, name='guess_the_habitat_two'),
    path('guess-the-habitat/level-three', views.guess_the_habitat_three, name='guess_the_habitat_three'),
]