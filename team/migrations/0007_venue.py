# Generated by Django 3.2.2 on 2021-05-10 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_alter_team_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('parent_id', models.PositiveSmallIntegerField(null=True)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venue', to='team.team')),
            ],
        ),
    ]