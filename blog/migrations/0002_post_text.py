# Generated by Django 5.2.3 on 2025-06-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="text",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
