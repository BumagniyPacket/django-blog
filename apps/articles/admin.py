from django.contrib import admin

from .models import Article


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'draft')
    list_filter = ('timestamp', 'category', 'tags')
    search_fields = ('title', 'description', 'content')
    fields = (
        'title', 'category', 'tags', 'image', 'description', 'content', 'draft'
    )

    class Meta:
        model = Article


admin.site.register(Article, PostModelAdmin)
