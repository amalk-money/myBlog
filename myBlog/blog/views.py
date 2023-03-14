from django.shortcuts import render, HttpResponse

def blogHome(request):
    return HttpResponse("<h3>This is blogHome. We will keep all post here.</h3>")

def blogPost(request, slug):
    return HttpResponse(f"<h3>This is blogPost: {slug}</h3>")