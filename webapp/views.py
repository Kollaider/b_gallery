from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def blog(request):
    return render(request, 'webapp/blog.html')


def about(request):
    return render(request, 'webapp/about.html')

def gallery(request):
    return render(request, 'webapp/gallery.html')

def gallery_single(request):
    return render(request, 'webapp/gallery-single.html')