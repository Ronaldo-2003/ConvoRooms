from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def coreHome(request):
    return HttpResponse('<h3>Hi user , you are at home page of coreApp.</h3>')