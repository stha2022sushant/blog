# Generated by Django 5.1.4 on 2025-01-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApplication', '0004_rename_itle_blogapp_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruit',
            name='color',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Fruit',
        ),
    ]
