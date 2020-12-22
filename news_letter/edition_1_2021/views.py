from django.shortcuts import render
from django.http import HttpResponse


def edition_1_2021_home(request):
    return render(request, 'edition_1_2021/home.html')

def edition_1_2021_content_tech(request):
    return render(request, 'edition_1_2021/content_tech.html')

def edition_1_2021_content_non_tech(request):
    return render(request, 'edition_1_2021/content_non_tech.html')

def edition_1_2021_content_book(request):
    return render(request, 'edition_1_2021/content_book.html')

def edition_1_2021_images(request):
    return render(request, 'edition_1_2021/images.html')
