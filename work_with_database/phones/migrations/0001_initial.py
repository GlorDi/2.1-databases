# Generated by Django 4.2.7 on 2023-11-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField()),
                ('image', models.URLField()),
                ('release_date', models.DateField(max_length=255)),
                ('lte_exists', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
    ]
