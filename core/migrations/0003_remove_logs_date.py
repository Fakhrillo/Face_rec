# Generated by Django 4.2.4 on 2023-08-18 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_users_employees_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='date',
        ),
    ]
