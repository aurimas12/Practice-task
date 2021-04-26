# Generated by Django 3.2 on 2021-04-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Assistant'), (3, 'User')]),
        ),
    ]