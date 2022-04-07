from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Recipe, RecipeIngredient


User = get_user_model()


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ('quantity_as_float', 'as_mks', 'as_imperial',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', )
    readonly_fields = ('timestamp', 'updated',)
    raw_id_fields = ('user',)
    inlines = (RecipeIngredientInline, )


admin.site.register(Recipe, RecipeAdmin)




