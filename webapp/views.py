from django.shortcuts import render
from djang.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h2>HEY!<h2>")