# Generated by Django 4.1.7 on 2023-04-25 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='grand_total',
        ),
    ]
