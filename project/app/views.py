from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Welcome to my app........... home page</h1>")
