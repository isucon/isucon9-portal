# Generated by Django 2.2.2 on 2019-06-24 03:27

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_team_aggregated_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='media/icons/'),
        ),
    ]
