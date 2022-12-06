# Generated by Django 4.1.3 on 2022-12-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_question_question_text_alter_question_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='content',
        ),
        migrations.RemoveField(
            model_name='option',
            name='options',
        ),
        migrations.AddField(
            model_name='option',
            name='optionA',
            field=models.CharField(default=0, max_length=40, verbose_name='A'),
        ),
        migrations.AddField(
            model_name='option',
            name='optionB',
            field=models.CharField(default=0, max_length=40, verbose_name='B'),
        ),
        migrations.AddField(
            model_name='option',
            name='optionC',
            field=models.CharField(default=0, max_length=40, verbose_name='C'),
        ),
        migrations.AddField(
            model_name='option',
            name='optionD',
            field=models.CharField(default=0, max_length=40, verbose_name='D'),
        ),
    ]
