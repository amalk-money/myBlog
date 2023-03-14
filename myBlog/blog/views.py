from django.shortcuts import render, HttpResponse

def index(index):
    return HttpResponse("<h1>Hi There! This is blog page</h1>")