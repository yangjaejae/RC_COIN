# Generated by Django 2.1.2 on 2018-12-04 00:48

from django.db import migrations
import store.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20181204_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=store.fields.ThumbnailImageField(upload_to='store\\<django.db.models.fields.related.ForeignKey>'),
        ),
    ]