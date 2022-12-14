# Generated by Django 4.1 on 2022-09-02 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCategory', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'productCategory',
                'verbose_name_plural': 'productCategory',
            },
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProduct', models.CharField(max_length=100)),
                ('imageProduct', models.ImageField(upload_to='store')),
                ('statusProduct', models.BooleanField(default=True)),
                ('priceProduct', models.FloatField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStore.productcategory')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
