# Generated by Django 3.0.4 on 2021-01-14 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0005_product_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="profile",
        ),
        migrations.AddField(
            model_name="product",
            name="uploaded_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
