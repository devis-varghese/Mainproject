# Generated by Django 4.1.3 on 2022-11-12 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='why_title',
        ),
    ]
