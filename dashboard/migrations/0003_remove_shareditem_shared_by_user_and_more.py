# Generated by Django 4.2 on 2023-04-27 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_shareditem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareditem',
            name='shared_by_user',
        ),
        migrations.RemoveField(
            model_name='shareditem',
            name='shared_to_emails',
        ),
    ]
