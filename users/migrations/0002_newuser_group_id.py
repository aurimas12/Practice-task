# Generated by Django 3.2 on 2021-04-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='group_id',
            field=models.ManyToManyField(blank=True, to='group.Group'),
        ),
    ]