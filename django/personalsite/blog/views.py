from django.shortcuts import render
from blog.models import Post, Comment, User

# Create your views here.

def blog(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'album/index.html', context)
