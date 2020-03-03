from django import template
from ..forms import CommentForm
from TestModel.models import Post
from ..models import Comment

register = template.Library()


@register.inclusion_tag('blog/inclusion/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post
    }


@register.inclusion_tag('blog/inclusion/_list.html', takes_context=True)
def show_commens(context, post):
    comment_list = Comment.objects.filter(post=post).order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }
