# Generated by Django 2.2.6 on 2019-10-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='url2',
            field=models.URLField(verbose_name='site URL2'),
        ),
    ]
