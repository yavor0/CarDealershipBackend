# Generated by Django 4.0.4 on 2022-05-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_alter_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
