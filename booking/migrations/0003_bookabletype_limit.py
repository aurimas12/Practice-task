# Generated by Django 3.2 on 2021-04-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_bookable_team_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookabletype',
            name='limit',
            field=models.PositiveSmallIntegerField(default=12),
        ),
    ]