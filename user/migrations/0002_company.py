# Generated by Django 3.0.4 on 2021-01-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Unique value for company URL, created from name.",
                        unique=True,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
    ]
