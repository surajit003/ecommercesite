# Generated by Django 3.0.4 on 2021-01-14 08:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_userprofile_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="profile_id",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]