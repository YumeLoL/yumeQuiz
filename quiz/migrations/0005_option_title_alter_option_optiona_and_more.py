# Generated by Django 4.1.3 on 2022-12-06 12:38

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_option_content_remove_option_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], default='', max_length=9, verbose_name='Quiz Type'),
        ),
        migrations.AlterField(
            model_name='option',
            name='optionA',
            field=models.CharField(default='', max_length=40, verbose_name='A'),
        ),
        migrations.AlterField(
            model_name='option',
            name='optionB',
            field=models.CharField(default='', max_length=40, verbose_name='B'),
        ),
        migrations.AlterField(
            model_name='option',
            name='optionC',
            field=models.CharField(default='', max_length=40, verbose_name='C'),
        ),
        migrations.AlterField(
            model_name='option',
            name='optionD',
            field=models.CharField(default='', max_length=40, verbose_name='D'),
        ),
    ]
