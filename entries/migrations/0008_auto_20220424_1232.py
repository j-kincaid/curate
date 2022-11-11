# Generated by Django 3.2.13 on 2022-04-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("entries", "0007_auto_20220424_1230"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artwork",
            old_name="dimensions",
            new_name="depth",
        ),
        migrations.AddField(
            model_name="artwork",
            name="height",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="artwork",
            name="width",
            field=models.IntegerField(default=0),
        ),
    ]
