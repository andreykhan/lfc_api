# Generated by Django 4.1 on 2022-08-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.TextField()),
                ('age', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
    ]
