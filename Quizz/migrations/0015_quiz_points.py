# Generated by Django 2.2.3 on 2019-07-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0014_auto_20190728_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]