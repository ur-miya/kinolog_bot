# Generated by Django 4.2 on 2023-04-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinolog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kinolog',
            old_name='full_name',
            new_name='name',
        ),
    ]
