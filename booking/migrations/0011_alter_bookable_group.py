# Generated by Django 3.2 on 2021-04-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('booking', '0010_alter_bookable_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookable',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='group.Group'),
        ),
    ]