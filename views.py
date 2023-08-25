from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html', {'name': 'hammed' })



def signup(request):
    return render(request, 'signup.html', {'name': 'hammed' })


def my_view(request):
    font_awesome_url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css"
    return render(request, 'head.html', {'font_awesome_url': font_awesome_url})

def header(request):
    return render(request, 'header.html', {'name': 'hammed' })

def side(request):
    return render(request, 'side.html', {'name': 'hammed' })


def home(request):
    return render(request, 'home.html', {'name': 'hammed' })


