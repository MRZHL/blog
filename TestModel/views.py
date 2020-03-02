from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
import markdown
import re
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify


# Create your views here.

def index(request):
    # - 表示的是逆序
    postlist = Post.objects.all().order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'postlist': postlist,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 将 markdown 文本解析为 html

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify)

    ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={
        'post': post
    })


# 通过时间获取不到信息的一个原因是,MYSQL 需要设置USE_TZ = False ,默认是True, 在Setting.py 中
def archive(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'postlist': post_list
    })


# 根据分类的 id 取列表
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    postlist = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'postlist': postlist,
    })


def tag(request,pk):
    # 这里一定是 pk=pk 不是 id
    ta = get_object_or_404(Tag,pk=pk)
    postlist = Post.objects.filter(tag=ta).order_by('-create_time')
    return render(request, template_name='blog/index.html', context={
        'postlist': postlist
    })