# Generated by Django 4.1.3 on 2022-11-12 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_why_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='emi_start_price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]