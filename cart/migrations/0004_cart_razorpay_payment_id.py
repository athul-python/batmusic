# Generated by Django 4.1.7 on 2023-04-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_razorpay_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
