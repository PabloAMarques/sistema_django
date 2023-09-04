# Generated by Django 4.2.4 on 2023-09-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proposal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("document", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("approved", models.BooleanField(default=False)),
            ],
        ),
    ]