# Generated by Django 3.1.3 on 2020-11-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(default=5),
        ),
    ]
