from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
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
    if len(query) > 80:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)

    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html',params)

def handleSignUp(request):
    if request.method == 'POST':
        #Get the parameters
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #check/validate input data
        #username under 10 char
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('home')
        #username must not contain special characters
        if not username.isalnum():
            messages.error(request, "Username must not contain special characters.")
            return redirect('home')
        #check passwords
        if password1 != password2:
            messages.error(request, "Please enter correct password.")
            return redirect('home')

        #create user
        user1 = User.objects.create_user(username, email, password1)
        user1.save()

        messages.success(request, "Your account has been successfully been created.")
        return redirect('/')

    else:
        return HttpResponse("404: Page not found.")