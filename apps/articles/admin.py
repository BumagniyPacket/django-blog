from django.contrib import admin

from .models import Article, Tag


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'draft')
    list_filter = ('timestamp', 'category', 'tags')
    search_fields = ('title', 'description', 'content')
    fields = (
        'title', 'category', 'tags', 'image', 'description', 'content', 'draft'
    )

    class Meta:
        model = Article


class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
        fields = '__all__'


admin.site.register(Article, PostModelAdmin)
admin.site.register(Tag, TagAdmin)
