from django import template

from ..forms import CommentForm
from ..models import Comment

register = template.Library()


@register.inclusion_tag(filename='comments/comments_wrap.html')
def comments(post_id, is_superuser):
    if is_superuser:
        comments_list = Comment.objects.filter(post_id=post_id)
    else:
        comments_list = Comment.objects.approved(post_id=post_id)
    comments_list = comments_list.order_by('-timestamp')

    form = CommentForm(initial={'post': post_id})
    context = {
        'comments': comments_list,
        'form': form,
        'edit_comment': is_superuser
    }
    return context
