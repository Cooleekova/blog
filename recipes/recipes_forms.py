from django import forms

from .models import Recipe, RecipeIngredient


""" django-crispy-forms"""


class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    name = forms.CharField(help_text='This is your help!')
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #   'class': 'form-control', 'placeholder': 'the name of the recipe'
    # }))
    # description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'rows': 2})
        self.fields['directions'].widget.attrs.update({'rows': 4})
        for field in self.fields:
            new_data = {
                "placeholder": f'Recipe {str(field)}',
                # "hx-post": ".",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit']
