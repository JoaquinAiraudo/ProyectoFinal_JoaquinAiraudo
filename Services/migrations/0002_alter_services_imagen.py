# Generated by Django 4.0.3 on 2022-07-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='imagen',
            field=models.ImageField(upload_to='Services'),
        ),
    ]
