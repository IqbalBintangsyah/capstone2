from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests
from django.http import HttpResponse

def about(request):
    context = {
        'hero':'Tentang',
    }
    return render(request,'about/website.html', {})

def team(request):
    return render(request,'about/team.html', {})

def informasigunung(request):
    return render(request,'about/informasigunung.html', {})