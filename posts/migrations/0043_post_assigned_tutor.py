# Generated by Django 4.1.3 on 2023-03-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0042_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='assigned_tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_posts', to='posts.tutor'),
        ),
    ]
