# Generated by Django 2.1.4 on 2019-01-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0002_auto_20190108_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
