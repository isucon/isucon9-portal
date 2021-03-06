# Generated by Django 2.2.1 on 2019-08-09 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_auto_20190805_1626'),
        ('contest', '0006_auto_20190806_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='servers', to='authentication.Team', verbose_name='チーム'),
        ),
        migrations.AlterUniqueTogether(
            name='server',
            unique_together={('team', 'hostname')},
        ),
    ]
