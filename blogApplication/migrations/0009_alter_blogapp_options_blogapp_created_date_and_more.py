# Generated by Django 5.1.5 on 2025-01-23 10:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApplication', '0008_alter_blogapp_options_remove_blogapp_created_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogapp',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='blogapp',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogapp',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
