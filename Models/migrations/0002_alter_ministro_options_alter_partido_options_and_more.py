# Generated by Django 4.0.3 on 2022-07-21 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ministro',
            options={'verbose_name': 'Ministro', 'verbose_name_plural': 'Ministros'},
        ),
        migrations.AlterModelOptions(
            name='partido',
            options={'verbose_name': 'Partido', 'verbose_name_plural': 'Partidos'},
        ),
        migrations.AlterModelOptions(
            name='presidente',
            options={'verbose_name': 'Presidente', 'verbose_name_plural': 'Presidentes'},
        ),
    ]
