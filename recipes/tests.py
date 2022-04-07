from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Create your tests here.


from .models import Recipe, RecipeIngredient

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('Pavel', password='Pavel1991')

    def test_user_password(self):
        checked = self.user_a.check_password('Pavel1991')
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('Pavel', password='Pavel1991')
        self.recipe_a = Recipe.objects.create(
            name='Pasta',
            user=self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Salad',
            user=self.user_a
        )
        self.recipe_ingridient_a = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Noodles',
            quantity='200',
            unit='grams'
        )
        self.recipe_ingridient_b = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name='Salt',
            quantity='по вкусу',
            unit='grams'
        )

    def test_user_recipe_reverse_count(self):
        qs = self.user_a.recipe_set.all()
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_count(self):
        qs = Recipe.objects.filter(user=self.user_a)
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_ingredient_reverse_count(self):
        qs = self.recipe_a.recipeingredient_set.all()
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_ingredient_count(self):
        qs = RecipeIngredient.objects.filter(recipe=self.recipe_a)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        qs = RecipeIngredient.objects.filter(recipe__user=self.user_a)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_reverse_relation(self):
        ids = list(self.user_a.recipe_set.all().values_list('recipeingredient__id', flat=True))
        qs = RecipeIngredient.objects.filter(id__in=ids)
        self.assertEqual(qs.count(), 2)

    def test_unit_measure_validation_error(self):
        invalid_unit = 'abc'
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                name='NEW',
                recipe=self.recipe_b,
                quantity=10,
                unit=invalid_unit
            )
            ingredient.full_clean()

    def test_unit_measure_validation(self):
        valid_unit = 'kg'
        ingredient = RecipeIngredient(
            name='NEW',
            recipe=self.recipe_b,
            quantity=10,
            unit=valid_unit
        )
        ingredient.full_clean()

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingridient_a.quantity_as_float)
        self.assertIsNone(self.recipe_ingridient_b.quantity_as_float)
