# Generated by Django 3.1.3 on 2021-01-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20201227_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
