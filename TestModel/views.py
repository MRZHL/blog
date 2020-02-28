from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
    # - 表示的是逆序
    postlist = Post.objects.all().order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'postlist': postlist,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={
        'post': post
    })
