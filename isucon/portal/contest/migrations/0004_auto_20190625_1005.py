# Generated by Django 2.2.2 on 2019-06-25 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_auto_20190621_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='log_text',
            field=models.TextField(blank=True, verbose_name='ログ文字列'),
        ),
        migrations.AlterField(
            model_name='job',
            name='result_json',
            field=models.TextField(blank=True, verbose_name='結果JSON'),
        ),
    ]
