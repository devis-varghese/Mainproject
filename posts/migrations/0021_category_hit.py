# Generated by Django 4.1.3 on 2022-11-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_remove_category_hit'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
