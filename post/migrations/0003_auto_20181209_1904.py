# Generated by Django 2.1.4 on 2018-12-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20181206_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текст коментаря:'),
        ),
    ]
