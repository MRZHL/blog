from django import template
from ..models import Post, Tag, Category

register = template.Library()


# True 表示设置为 True 时将告诉 django，在渲染 _recent_posts.html 模板时，不仅传入show_recent_posts 返回的模板变量，同时会传入父模板
@register.inclusion_tag('blog/inclusion/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-create_time')[:num]
    }


@register.inclusion_tag('blog/inclusion/_archive.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.all().dates('create_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusion/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.all()
    for cat in category_list:
        postlist = Post.objects.filter(category=cat)
        cat.count = postlist.count()
    return {
        'category_list': category_list,
    }


@register.inclusion_tag('blog/inclusion/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all()
    }
