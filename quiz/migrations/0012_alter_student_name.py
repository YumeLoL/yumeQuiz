# Generated by Django 4.1.3 on 2022-12-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_alter_student_pwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default=None, max_length=200, unique=True, verbose_name='Student Name'),
        ),
    ]
