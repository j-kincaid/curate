# Generated by Django 3.2.13 on 2022-05-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0018_artist"),
    ]

    operations = [
        migrations.AddField(
            model_name="artwork",
            name="medium",
            field=models.CharField(
                choices=[
                    ("PA", "Painting"),
                    ("SC", "Sculpture"),
                    ("PH", "Photography"),
                    ("CE", "Ceramic"),
                    ("TX", "Textile"),
                    ("PT", "Print"),
                    ("DG", "Digital"),
                    ("OT", "Other"),
                ],
                max_length=2,
                null=True,
            ),
        ),
    ]
