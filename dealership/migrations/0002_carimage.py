# Generated by Django 4.0.4 on 2022-05-09 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dealership/images')),
                ('Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dealership.car')),
            ],
        ),
    ]
