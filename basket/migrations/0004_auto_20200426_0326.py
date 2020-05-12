# Generated by Django 3.0.1 on 2020-04-26 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_auto_20200425_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Basket', 'verbose_name_plural': 'Baskets'},
        ),
        migrations.AlterModelOptions(
            name='basketitem',
            options={'verbose_name': 'Basket item', 'verbose_name_plural': 'Basket items'},
        ),
        migrations.AddField(
            model_name='basket',
            name='total',
            field=models.FloatField(default=0.0, verbose_name='Total amount'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='basketitem',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='basket.Basket'),
        ),
    ]