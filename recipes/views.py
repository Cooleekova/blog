from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.forms.models import modelformset_factory
# Create your views here.
from django.urls import reverse

from .models import Recipe, RecipeIngredient
from .recipes_forms import RecipeForm, RecipeIngredientForm


""" CRUD - Create Retrieve Update Delete """


@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list': qs
    }
    return render(request, 'recipes/list.html', context)


@login_required
def recipe_detail_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse('<h1 style="color:red">Not found</h1>')
        raise Http404
    context = {
        'object': obj
    }
    if request.htmx:

        return render(request, 'recipes/partials/detail.html', context)
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_delete_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not found")
        raise Http404
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipes:list')
        if request.htmx:
            headers = {
                'HX-Redirect': success_url
            }
            return HttpResponse('Success', headers=headers)
        return redirect(success_url)
    context = {
        'object': obj
    }
    return render(request, 'recipes/delete.html', context)


@login_required
def recipe_ingredient_delete_view(request, parent_id=None, id=None):
    try:
        obj = RecipeIngredient.objects.get(id=id, recipe__id=parent_id, recipe__user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not found")
        raise Http404
    if request.method == "POST":
        obj.delete()
        success_url = reverse('recipes:detail', kwargs={'id': parent_id})
        if request.htmx:
            name = obj.name
            return render(request, 'recipes/partials/ingredient-inline-delete-response.html', {'name': name})

        return redirect(success_url)
    context = {
        'object': obj
    }
    return render(request, 'recipes/delete.html', context)



@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    # create_ingredient_url = reverse('recipes:hx-ingredient-create', kwargs={'parent_id': id})
    context = {
        'form': form,
        # 'create_ingredient_url': create_ingredient_url
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)
        return redirect(obj.get_absolute_url())
    return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    create_ingredient_url = reverse('recipes:hx-ingredient-create', kwargs={'parent_id': id})
    context = {
        'form': form,
        'object': obj,
        'create_ingredient_url': create_ingredient_url
    }

    if form.is_valid():
        form.save()
        context['message'] = 'the recipe was saved'

    if request.htmx:
        return render(request, 'recipes/partials/forms.html', context)

    return render(request, 'recipes/create-update.html', context)



@login_required
def recipe_ingredient_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse('<h1 style="color:red">Not found</h1>')

    instance = None
    if id is not None:
        try:
            instance = RecipeIngredient.objects.get(recipe=parent_obj, id=id)
        except:
            instance = None
    form = RecipeIngredientForm(request.POST or None, instance=instance)
    url = instance.get_hx_update_url if instance else reverse('recipes:hx-ingredient-create', kwargs={'parent_id': parent_id})
    context = {
        'object': instance,
        'form': form,
        'url': url
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['object'] = new_obj
        return render(request, 'recipes/partials/ingredient-inline.html', context)

    return render(request, 'recipes/partials/ingredient-form.html', context)





""" This is an old view with formset and without HTMX"""

# @login_required
# def recipe_update_view(request, id=None):
#     obj = get_object_or_404(Recipe, id=id, user=request.user)
#     form = RecipeForm(request.POST or None, instance=obj)
#     RecipeIngredientFormset = modelformset_factory(RecipeIngredient, form=RecipeIngredientForm, extra=0)
#     formset = RecipeIngredientFormset(request.POST or None, queryset=obj.get_ingredients_children())
#     context = {
#         'form': form,
#         'formset': formset,
#         'object': obj
#     }
#
#     if all([form.is_valid(), formset.is_valid()]):
#         parent = form.save(commit=False)
#         parent.save()
#         for form in formset:
#             child = form.save(commit=False)
#             child.recipe = parent
#             child.save()
#         context['message'] = 'the recipe was saved'
#
#     if request.htmx:
#         return render(request, 'recipes/partials/forms.html', context)
#
#     return render(request, 'recipes/create-update.html', context)
