from django.contrib import admin

# Register your models here.

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'slug', 'date_created', 'id')
    search_fields = ('title', 'text')
    raw_id_fields = ('user', )

