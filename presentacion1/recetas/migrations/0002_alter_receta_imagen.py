# Generated by Django 4.1.2 on 2022-10-22 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
