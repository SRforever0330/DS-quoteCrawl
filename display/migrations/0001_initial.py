# Generated by Django 4.0.6 on 2022-07-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=1000)),
                ('author_born_date', models.CharField(max_length=1000)),
                ('author_born_location', models.CharField(max_length=1000)),
                ('author_description', models.TextField()),
            ],
        ),
    ]
