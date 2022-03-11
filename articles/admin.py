from django.contrib import admin

# Register your models here.

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    search_fields = ('title', 'text')

# heroku run python manage.py migrate

# python manage.py dumpdata articles > D:\Nethology\articles\blog\articles\fixtures\DUMP.json

# python manage.py dumpdata articles > DB_data.json

# heroku run python manage.py loaddata D:\Nethology\articles\blog\articles\fixtures\DUMP.json


# heroku run python manage.py loaddata D:\Nethology\articles\blog\articles\fixtures\DUMP.json
# D:\Nethology\articles\blog\articles\fixtures\DUMP.json
# heroku run python manage.py loaddata articles/fixtures/DUMP.json