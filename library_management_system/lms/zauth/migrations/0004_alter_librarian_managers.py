# Generated by Django 5.0.6 on 2024-06-22 08:03

import zauth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zauth', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='librarian',
            managers=[
                ('objects', zauth.models.ZUserManager()),
            ],
        ),
    ]
