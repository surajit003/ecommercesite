# Generated by Django 3.0.4 on 2021-01-14 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.Company",
            ),
        ),
    ]
