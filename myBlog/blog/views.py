from django.shortcuts import render, HttpResponse

def home(index):
    return HttpResponse("<h1>Hi There! This is blog home page</h1>")
def blog(index):
    return HttpResponse("<h1>Hi There! This is blog page</h1>")