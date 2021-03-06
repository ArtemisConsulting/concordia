# Generated by Django 2.0.8 on 2018-09-04 17:58

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("concordia", "0013_auto_20180826_0928")]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("item_url", models.URLField(max_length=255)),
                ("item_id", models.CharField(blank=True, max_length=100)),
                (
                    "metadata",
                    django.contrib.postgres.fields.jsonb.JSONField(default=dict),
                ),
                ("thumbnail_image", models.URLField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Edit", "Open for Edit"),
                            ("Submitted", "Submitted for Review"),
                            ("Completed", "Transcription Completed"),
                            ("Inactive", "Inactive"),
                            ("Active", "Active"),
                        ],
                        default="Edit",
                        max_length=10,
                    ),
                ),
                ("is_publish", models.BooleanField(default=False)),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.Campaign",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="concordia.Project",
                    ),
                ),
            ],
            options={"ordering": ["item_id"]},
        ),
        migrations.AlterModelOptions(
            name="asset", options={"ordering": ["item", "sequence"]}
        ),
        migrations.AddField(
            model_name="asset",
            name="item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="concordia.Item",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="item", unique_together={("item_id", "campaign")}
        ),
    ]
