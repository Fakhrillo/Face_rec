# Generated by Django 4.2.4 on 2023-08-21 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_logs_conf_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='conf_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]