# Generated by Django 2.2.6 on 2019-11-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='data',
            field=models.CharField(max_length=100),
        ),
    ]
