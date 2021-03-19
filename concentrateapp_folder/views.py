from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'concentrateapp_folder/index.html')


def about_us(request):
    return render(request, 'concentrateapp_folder/about_us.html')