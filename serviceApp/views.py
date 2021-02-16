from django.shortcuts import render
from django.http import HttpResponse, request

def lead(request):
    return render(request,'lead.html')


def screen2(request):
    return render(request, 'screen2.html')

def screen3(request):
    return render(request, 'screen3.html')

