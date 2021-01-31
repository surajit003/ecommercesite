# Generated by Django 3.0.4 on 2021-01-05 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0001_initial"),
        ("payment", "0001_initial"),
        ("order", "0002_auto_20210105_1024"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="billing_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="billing_address",
                to="checkout.Address",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="payment.Payment",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shipping_address",
                to="checkout.Address",
            ),
        ),
    ]