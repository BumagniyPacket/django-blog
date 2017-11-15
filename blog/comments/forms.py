from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'text',)
        widgets = {'post': forms.HiddenInput()}
