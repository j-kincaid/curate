# Generated by Django 3.2.13 on 2022-07-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0022_auto_20220705_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='height_in_feet',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]