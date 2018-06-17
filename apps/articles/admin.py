from django.contrib import admin

from .models import Article, Category


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'draft')
    list_filter = ('timestamp',)
    search_fields = ('title', 'description', 'content')
    fields = ('title', 'category', 'image', 'description', 'content', 'draft')

    class Meta:
        model = Article


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
        fields = '__all__'


admin.site.register(Article, PostModelAdmin)
admin.site.register(Category, CategoryAdmin)
