# Generated by Django 2.1.2 on 2018-11-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20181125_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='domain',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc',
            field=models.CharField(max_length=20),
        ),
    ]