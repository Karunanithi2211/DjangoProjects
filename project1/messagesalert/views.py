from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def message(r):
    return render(r,'message.html')

def success(r):
    messages.success(r,'This is success alert')
    return render(r,'message.html')

def info(r):
    messages.info(r,'This is Info alert')
    return render(r,'message.html')

def warning(r):
    messages.warning(r,'This is warning alert')
    return render(r,'message.html')

def danger(r):
    messages.error(r,'This is Danger alert')
    return render(r,'message.html')