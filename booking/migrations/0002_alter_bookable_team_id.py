# Generated by Django 3.2 on 2021-04-20 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_delete_student'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookable',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
    ]