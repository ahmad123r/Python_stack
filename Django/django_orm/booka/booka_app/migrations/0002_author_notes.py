# Generated by Django 2.2.4 on 2021-05-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booka_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
