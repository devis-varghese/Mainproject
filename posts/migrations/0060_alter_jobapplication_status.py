# Generated by Django 4.1.3 on 2023-04-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0059_liveclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('interviewscheduled', 'Interviewscheduled'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=20),
        ),
    ]
