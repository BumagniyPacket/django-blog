from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
        fields = '__all__'


admin.site.register(Tag, TagAdmin)
