from django.shortcuts import render

from .models import Article
# Create your views here.


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj
    }
    return render(request, 'articles/detail.html', context=context)


def article_search_view(request):
    query_dict = request.GET  # this is a dictionary
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_object = None
    if query is not None:
        article_object = Article.objects.get(id=query)
    context = {
        'object': article_object,
    }
    return render(request, 'articles/search.html', context=context)


def article_create_view(request):
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        article_object = Article.objects.create(title=title, text = text)
        context = {
            "object": article_object,
            "created": True
        }
    return render(request, 'articles/create.html', context=context)
