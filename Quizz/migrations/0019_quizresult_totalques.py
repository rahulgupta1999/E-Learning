# Generated by Django 2.2.3 on 2019-07-31 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0018_auto_20190730_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizresult',
            name='totalQues',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
