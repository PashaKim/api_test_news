# Generated by Django 3.0.7 on 2020-06-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
