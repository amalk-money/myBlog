from django.shortcuts import render, HttpResponse

def index(index):
    return HttpResponse("<h1>Hi There! How are you doing</h1>")

