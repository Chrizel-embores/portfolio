# base/views.py
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, 'base/home.html')

def portfolio_details(request):
    return render(request, 'base/portfolio-details.html')

