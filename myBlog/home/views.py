from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h3>This is home page</h3>")

def contact(request):
    return HttpResponse("<h3>This is contact page</h3>")

def about(request):
    return HttpResponse("<h3>This is about page</h3>")