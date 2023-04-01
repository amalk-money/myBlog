from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, Comments
def blogHome(request):
    allPosts = Post.objects.all()
    params = {'allPosts': allPosts}
    return render(request, 'blog/blogHome.html', params)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Comments.objects.filter(post=post)
    param = {'post': post, 'comments': comments}
    return render(request, 'blog/blogPost.html', param)

from django.contrib import messages
def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postsno = request.POST.get('postSNo')
        post = Post.objects.get(postID=postsno)

        comment = Comments(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comments posted.")

    return redirect(f"/blog/{post.slug}/")