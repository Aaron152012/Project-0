from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Search(request):
    return render(request, "Search/Project 0.html")