# Generated by Django 4.1 on 2022-09-05 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appStore', '0003_alter_products_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='update',
            new_name='updated',
        ),
    ]
