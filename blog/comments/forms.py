from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('article', 'author', 'text',)
        widgets = {'article': forms.HiddenInput()}
