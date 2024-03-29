# Generated by Django 2.1.12 on 2019-09-24 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=250)),
                ('detail', models.CharField(max_length=250)),
                ('img_url', models.CharField(max_length=250)),
                ('github', models.CharField(max_length=250)),
                ('meta', models.ManyToManyField(to='core.Meta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
