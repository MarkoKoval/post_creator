# Generated by Django 2.0 on 2019-02-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190223_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='desciption',
            field=models.CharField(blank=True, default='no description yet', max_length=500),
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, default='no title yet', max_length=64),
        ),
    ]
