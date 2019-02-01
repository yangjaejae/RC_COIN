# Generated by Django 2.0.10 on 2019-01-23 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.fields
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', store.fields.ThumbnailImageField(null=True, upload_to=store.models.upload_path_handler)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['store'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('corporate_number', models.CharField(max_length=12, null=True)),
                ('address', models.CharField(default='-', max_length=100, null=True)),
                ('phone_number', models.CharField(default='-', max_length=15, null=True)),
                ('url', models.CharField(default='-', max_length=100, null=True)),
                ('opening_hour', models.CharField(max_length=2, null=True)),
                ('opening_minute', models.CharField(max_length=2, null=True)),
                ('closing_hour', models.CharField(max_length=2, null=True)),
                ('closing_minute', models.CharField(max_length=2, null=True)),
                ('description', models.TextField(blank=True)),
                ('registered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=1, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Location')),
                ('representative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store'),
        ),
    ]
