# Generated by Django 4.1.3 on 2022-12-07 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='student',
            name='pwd',
            field=models.CharField(default='', max_length=20, verbose_name='Password'),
        ),
        migrations.AddField(
            model_name='student',
            name='sid',
            field=models.BigAutoField(default=None, primary_key=True, serialize=False, verbose_name='Student Id'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.BooleanField(choices=[(0, 'female'), (1, 'male')], default=0, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True, verbose_name='Student Name'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='Score')),
                ('rtime', models.DateTimeField(blank=True, null=True, verbose_name='Submit Time:')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_id', to='quiz.student', verbose_name='Student Id')),
            ],
        ),
    ]
