# Generated by Django 3.2 on 2021-04-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('booking', '0007_remove_bookabletype_meeting_room_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookable',
            name='group_id',
            field=models.ManyToManyField(to='group.Group'),
        ),
    ]
