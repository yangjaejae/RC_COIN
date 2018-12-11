# Generated by Django 2.1.2 on 2018-12-03 15:11

from django.db import migrations, models
import django.db.models.deletion
import store.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20181126_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', store.fields.ThumbnailImageField(upload_to='store/%Store.id/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
            options={
                'ordering': ['store'],
            },
        ),
    ]