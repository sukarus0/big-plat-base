# Generated by Django 4.0.5 on 2022-07-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigdatacomponent',
            name='access_point',
            field=models.CharField(default='http://...', max_length=100),
        ),
    ]