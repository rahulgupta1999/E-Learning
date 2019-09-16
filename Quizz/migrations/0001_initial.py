# Generated by Django 2.2.3 on 2019-07-24 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('instName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
            ],
        ),
    ]