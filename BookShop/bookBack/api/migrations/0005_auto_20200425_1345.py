# Generated by Django 3.0.4 on 2020-04-25 07:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('top_list', django.db.models.manager.Manager()),
            ],
        ),
    ]
