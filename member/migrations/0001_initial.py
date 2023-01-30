# Generated by Django 4.1.5 on 2023-01-24 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20, verbose_name="氏名")),
            ],
        ),
        migrations.CreateModel(
            name="ProjectRecord",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("start_date", models.DateField(null=True, verbose_name="開始日")),
                ("end_date", models.DateField(null=True, verbose_name="終了日")),
                (
                    "project_abstract",
                    models.CharField(max_length=50, verbose_name="案件概要"),
                ),
                (
                    "project_detail",
                    models.CharField(max_length=1000, verbose_name="案件詳細"),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="member.member",
                        verbose_name="社員",
                    ),
                ),
            ],
        ),
    ]
