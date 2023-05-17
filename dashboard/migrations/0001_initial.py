# Generated by Django 4.2 on 2023-04-27 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('survey', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('additional_note', models.TextField(blank=True)),
                ('geo_data', models.TextField()),
                ('has_route', models.BooleanField(default=False)),
                ('route', models.TextField()),
                ('status', models.CharField(default='todo', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('additional_note', models.TextField(blank=True)),
                ('geo_data', models.TextField()),
                ('status', models.CharField(default='todo', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drafted', models.BooleanField(default=False)),
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.note')),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='survey.survey')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
