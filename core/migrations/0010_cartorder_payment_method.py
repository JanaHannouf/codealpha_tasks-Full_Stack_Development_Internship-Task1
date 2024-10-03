# Generated by Django 5.1.1 on 2024-09-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_cartorder_address_cartorder_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='payment_method',
            field=models.CharField(choices=[('cash on delivery', 'Cash on Delivery'), ('credit card', 'Credit Card'), ('paypal', 'PayPal')], default='cash on delivery', max_length=30),
        ),
    ]
