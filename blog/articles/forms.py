from django import forms
from pagedown.widgets import PagedownWidget

from .models import Article


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))

    class Meta:
        model = Article
        fields = [
            'title',
            'image',
            'description',
            'content',
            'draft'
        ]
