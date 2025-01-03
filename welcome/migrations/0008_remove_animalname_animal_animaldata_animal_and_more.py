# Generated by Django 4.2 on 2023-05-06 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_animaldata_animalname_location_delete_animal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalname',
            name='animal',
        ),
        migrations.AddField(
            model_name='animaldata',
            name='animal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='welcome.location'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='count',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welcome.animalname'),
        ),
    ]
