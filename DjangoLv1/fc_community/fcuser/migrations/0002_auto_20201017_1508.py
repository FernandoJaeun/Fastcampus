# Generated by Django 3.1.2 on 2020-10-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='username',
            field=models.CharField(max_length=14),
        ),
    ]
