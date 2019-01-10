# Generated by Django 2.1.4 on 2019-01-10 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0004_remove_photo_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=3, null=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
    ]
