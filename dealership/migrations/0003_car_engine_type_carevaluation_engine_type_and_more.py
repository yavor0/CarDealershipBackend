# Generated by Django 4.0.4 on 2022-05-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0002_alter_car_transmission_alter_car_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('Бензинов', 'Бензинов'), ('Дизелов', 'Дизелов'), ('Електрически', 'Електрически'), ('Хибриден', 'Хибриден')], default='Бензинов', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carevaluation',
            name='engine_type',
            field=models.CharField(choices=[('Бензинов', 'Бензинов'), ('Дизелов', 'Дизелов'), ('Електрически', 'Електрически'), ('Хибриден', 'Хибриден')], default='Бензинов', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Ръчна', 'Ръчна'), ('Автоматична', 'Автоматична'), ('Полуавтоматична', 'Полуавтоматична')], max_length=50),
        ),
        migrations.AlterField(
            model_name='carevaluation',
            name='transmission',
            field=models.CharField(choices=[('Ръчна', 'Ръчна'), ('Автоматична', 'Автоматична'), ('Полуавтоматична', 'Полуавтоматична')], max_length=50),
        ),
    ]
