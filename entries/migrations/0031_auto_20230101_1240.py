# Generated by Django 3.2.13 on 2023-01-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0030_review_votes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="artwork",
            name="source_link",
        ),
        migrations.AddField(
            model_name="artwork",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default_image.jpg", null=True, upload_to=""
            ),
        ),
    ]
