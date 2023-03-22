from django.shortcuts import render, HttpResponse
from blog.models import Post

def blogHome(request):
    allPosts = Post.objects.all()
    params = {'allPosts':allPosts}
    return render(request, 'blog/blogHome.html', params)

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html', {'slug':slug,})