from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('hello world')

def index(request):
    sitename = 'Hello World'
    return render(request, 'index.html', {"sitename": sitename})