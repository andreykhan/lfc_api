# Generated by Django 4.1 on 2022-08-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_players_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.TextField()),
                ('age', models.IntegerField()),
                ('job_title', models.TextField()),
            ],
        ),
    ]