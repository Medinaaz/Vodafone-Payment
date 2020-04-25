# Generated by Django 3.0.1 on 2020-04-25 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Property name')),
            ],
            options={
                'verbose_name': 'Property option',
                'verbose_name_plural': 'Property options',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='product.PropertyOption', verbose_name='Option')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='product.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product property',
                'verbose_name_plural': 'Product properties',
                'ordering': ('product', 'option'),
                'unique_together': {('product', 'option')},
            },
        ),
    ]
