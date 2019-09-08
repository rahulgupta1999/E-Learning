# Generated by Django 2.2.3 on 2019-07-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0005_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instName', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dateofBirth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
    ]
