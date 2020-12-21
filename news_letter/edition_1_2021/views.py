from django.shortcuts import render
from django.http import HttpResponse


def edition_1_2021_home(request):
    return render(request, 'edition_1_2021/home.html')
