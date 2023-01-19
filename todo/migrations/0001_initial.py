# Generated by Django 4.1.5 on 2023-01-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('memo', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
