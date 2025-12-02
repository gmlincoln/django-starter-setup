from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Welcome to Django!!!")

def homePage(request):
    context = {
        "title": "Home",
        "message": "Welcome to Django Page!!!"
    }
    return render(request, "index.html", context)

