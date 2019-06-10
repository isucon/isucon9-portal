# Generated by Django 2.2.1 on 2019-05-31 09:50

from django.db import migrations, models
import django.db.models.deletion
import isucon.portal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IPアドレス')),
                ('network', models.CharField(max_length=100, verbose_name='ネットワークアドレス')),
                ('node', models.CharField(max_length=100, verbose_name='ノード')),
            ],
            options={
                'verbose_name': 'ベンチマーカー',
                'verbose_name_plural': 'ベンチマーカー',
            },
            bases=(isucon.portal.models.LogicalDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100, unique=True, verbose_name='ホスト名')),
                ('global_ip', models.CharField(max_length=100, unique=True, verbose_name='グローバルIPアドレス')),
                ('private_ip', models.CharField(max_length=100, verbose_name='プライベートIPアドレス')),
                ('private_network', models.CharField(max_length=100, verbose_name='プライベートネットワークアドレス')),
            ],
            options={
                'verbose_name': 'サーバ',
                'verbose_name_plural': 'サーバ',
            },
            bases=(isucon.portal.models.LogicalDeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ScoreHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='得点')),
                ('is_passed', models.BooleanField(default=False, verbose_name='正答フラグ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='authentication.Team', verbose_name='チーム')),
            ],
            options={
                'verbose_name': 'スコア履歴',
                'verbose_name_plural': 'スコア履歴',
                'ordering': ('-created_at',),
            },
        ),
    ]