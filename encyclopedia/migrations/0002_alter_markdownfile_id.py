# Generated by Django 5.0.7 on 2024-07-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markdownfile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
