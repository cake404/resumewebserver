# Generated by Django 2.1.5 on 2019-01-26 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0006_auto_20190126_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='tech_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
