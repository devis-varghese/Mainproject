# Generated by Django 4.1.3 on 2022-11-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_emi_start_price_remove_post_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='discount',
        ),
    ]