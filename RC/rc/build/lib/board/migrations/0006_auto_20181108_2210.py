# Generated by Django 2.1.2 on 2018-11-08 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_boardliker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardliker',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Board'),
        ),
        migrations.AlterField(
            model_name='boardliker',
            name='liker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
