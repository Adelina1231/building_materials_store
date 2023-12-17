# Generated by Django 5.0 on 2023-12-17 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='orders.orderstatus', verbose_name='Статус заказа'),
        ),
    ]
