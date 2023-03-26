from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post
def home(request):
    popular = Post.objects.all().order_by('-views').values()[:3]
    params = {'allPosts': popular}
    return render(request, 'home/home.html', params)

def contact(request):
    if (request.method == "POST"):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        query = request.POST['query']

        if len(name)<3 or len(email)<10 or len(phone)<10:
            messages.error(request, "Oops! Please enter the correct details.")
        else:
            contact = Contact(name=name, phone=phone, email=email, query=query)
            contact.save()
            messages.success(request, 'Success!!! Thanks '+name+" for submitting your query." )

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['search']
    allPosts = Post.objects.filter(content__icontains=query)
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html',params)