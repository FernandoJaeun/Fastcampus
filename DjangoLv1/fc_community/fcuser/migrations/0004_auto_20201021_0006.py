# Generated by Django 3.1.2 on 2020-10-20 15:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_auto_20201020_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='registered_dttm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='등록시간'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='useremail',
            field=models.EmailField(default=1, max_length=128, verbose_name='사용자 이메일'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='password',
            field=models.CharField(max_length=32, null=True, verbose_name='암호'),
        ),
        migrations.AlterField(
            model_name='test',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]