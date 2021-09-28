from django.shortcuts import render
from django.http import JsonResponse
from posts.models import Post
from django.forms.models import model_to_dict


# Create your views here.

def count(request):
    return JsonResponse({
        'count': Post.objects.count()
    })


def posts(request):
    qs = Post.objects.all()
    data = list(qs.values())
    return JsonResponse(data, safe=False)


def singlepost(request, id):
    post = Post.objects.get(pk=id)
    postdict = model_to_dict(post)
    return JsonResponse(postdict)
