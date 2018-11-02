# Generated by Django 2.1.2 on 2018-11-02 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0005_auto_20181102_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=100, verbose_name='EMAIL')),
                ('age', models.IntegerField(default=0, verbose_name='AGE')),
                ('gender', models.CharField(max_length=2, verbose_name='GENDER')),
                ('type', models.CharField(max_length=1, verbose_name='TYPE')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='CREATE_DATE')),
                ('status', models.CharField(default='Y', max_length=1, verbose_name='STATUS')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
