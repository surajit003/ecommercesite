# Generated by Django 3.0.4 on 2021-01-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0010_company_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
