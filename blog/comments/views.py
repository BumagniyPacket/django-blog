from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from blog.comments.models import Comment


@login_required
def comment_approve(request, pk):
    instance = Comment.objects.get(pk=pk)
    instance.approve()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def comment_delete(request, pk):
    instance = Comment.objects.get(pk=pk)
    instance.delete()
    return redirect(request.META.get('HTTP_REFERER'))
