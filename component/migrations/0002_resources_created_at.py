# Generated by Django 4.0.5 on 2022-07-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
