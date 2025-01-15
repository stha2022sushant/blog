# Generated by Django 5.1.4 on 2025-01-13 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApplication', '0005_remove_fruit_color_delete_color_delete_fruit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogapp',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='blogapp',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
