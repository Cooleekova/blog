
from django.shortcuts import render

# Create your views here.
from recipes.models import Recipe
from articles.models import Article

SEARCH_TYPE_MAPPING = {
    'article': Article,
    'articles': Article,
    'recipe': Recipe,
    'recipes': Recipe
}


def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    Klass = Recipe
    if search_type in SEARCH_TYPE_MAPPING:
        Klass = SEARCH_TYPE_MAPPING[search_type]
    qs = Klass.objects.search(query=query)

    context = {
        'queryset': qs
    }
    template = 'search/results-view.html'
    if request.htmx:
        context['queryset'] = qs[:5]
        template = 'search/partials/results.html'
    return render(request, template, context)
