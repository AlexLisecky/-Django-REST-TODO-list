# Generated by Django 3.2.9 on 2021-11-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
    ]