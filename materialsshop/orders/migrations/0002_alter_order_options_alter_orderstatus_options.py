# Generated by Django 5.0 on 2023-12-17 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'Статус заказа', 'verbose_name_plural': 'Статус заказов'},
        ),
    ]