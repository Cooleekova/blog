# Generated by Django 4.0.3 on 2022-04-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipeingredient_quantity_as_float'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(max_length=15),
        ),
    ]
