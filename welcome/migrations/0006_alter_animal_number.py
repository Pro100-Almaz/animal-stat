# Generated by Django 4.2 on 2023-05-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_remove_animal_location_animal_region_animal_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
