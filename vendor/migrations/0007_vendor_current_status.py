# Generated by Django 3.0.4 on 2021-01-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0006_vendor_reviewed_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="current_status",
            field=models.CharField(
                choices=[("open", "open"), ("taken", "taken"), ("closed", "closed")],
                default="open",
                max_length=30,
            ),
        ),
    ]
