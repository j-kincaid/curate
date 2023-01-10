# Generated by Django 3.2.13 on 2023-01-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0031_auto_20230101_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('one_star', 1), ('two_stars', 2), ('three_stars', 3), ('four_stars', 4), ('five_stars', 5)], max_length=200),
        ),
    ]