# Generated by Django 4.2.7 on 2023-11-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_question_correct_answer_question_option1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='percentage',
            field=models.FloatField(null=True),
        ),
    ]
