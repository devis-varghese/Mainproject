# Generated by Django 4.1.3 on 2022-11-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_remove_blog_category_remove_tcforblog_blank_page_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='faq',
        ),
    ]
