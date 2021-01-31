# Generated by Django 3.0.4 on 2021-01-14 11:16

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0009_auto_20210114_1104"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=None,
                default=1,
                force_format=None,
                keep_meta=True,
                quality=75,
                size=[120, 120],
                upload_to="",
            ),
            preserve_default=False,
        ),
    ]