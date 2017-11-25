from django import template

from ..forms import CommentForm
from ..models import Comment

register = template.Library()


@register.inclusion_tag(filename='comments/comments_wrap.html')
def comments(article_id, is_superuser):
    if is_superuser:
        comments_list = Comment.objects.filter(article_id=article_id)
    else:
        comments_list = Comment.objects.approved(article_id=article_id)
    comments_list = comments_list.order_by('-timestamp')

    form = CommentForm(initial={'article': article_id})
    context = {
        'comments': comments_list,
        'form': form,
        'edit_comment': is_superuser
    }
    return context
