# Generated by Django 3.2 on 2021-05-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_delete_bookablegroup'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookable',
            name='group_id',
            field=models.ManyToManyField(blank=True, to='group.Group'),
        ),
    ]
