# Generated by Django 4.1 on 2022-08-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appServices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
