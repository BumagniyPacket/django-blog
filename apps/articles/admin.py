from django.contrib import admin

from .models import Article


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'updated', 'draft')
    list_filter = ('timestamp',)
    search_fields = ('title', 'content')
    fields = ('title', 'image', 'description', 'content', 'draft')

    class Meta:
        model = Article


admin.site.register(Article, PostModelAdmin)
