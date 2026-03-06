from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def aboutUs (request):
   return HttpResponse ("This is my blog")
