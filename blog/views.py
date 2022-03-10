from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
import random


def home_view(request):
    number = random.randint(1, 3)
    article = Article.objects.get(id=number)
    article_queryset = Article.objects.all()
    print(article_queryset)
    name = 'Tanya'
    context = {
        'object_list': article_queryset,
        'object': article,
        # 'title': article.title,
        # 'id': article.id,
        # 'text': article.text
    }
    HTML_STRING = render_to_string('home.html', context=context)

    H1_Article = f'<h1>{article.title} (id: {article.id})</h1>'

    return HttpResponse(HTML_STRING)
