from django.contrib import admin

from .models import Article, Category, Tag


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'draft')
    list_filter = ('timestamp', 'tags')
    search_fields = ('title', 'description', 'content')
    fields = ('title', 'category', 'tags', 'image', 'description', 'content',
              'draft')

    class Meta:
        model = Article


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = '__all__'


class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
        fields = '__all__'


admin.site.register(Article, PostModelAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
