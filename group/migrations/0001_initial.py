# Generated by Django 3.2 on 2021-04-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('issystem', models.BooleanField(default=False)),
                ('isvisible', models.BooleanField(default=False)),
            ],
        ),
    ]
