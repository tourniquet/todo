# Generated by Django 4.1.3 on 2023-01-12 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_entry_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='due_by',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 20, 26, 54, 975681)),
        ),
    ]
