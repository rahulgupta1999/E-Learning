# Generated by Django 2.2.3 on 2019-07-27 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0007_subject_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instName', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=50)),
                ('ans1', models.CharField(max_length=50)),
                ('ans2', models.CharField(max_length=50)),
                ('ans3', models.CharField(max_length=50)),
                ('ans4', models.CharField(max_length=50)),
                ('correct', models.CharField(max_length=50)),
            ],
        ),
    ]
