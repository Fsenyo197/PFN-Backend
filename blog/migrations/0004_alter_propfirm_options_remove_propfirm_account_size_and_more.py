# Generated by Django 5.1 on 2024-10-26 14:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_propfirm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propfirm',
            options={},
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='account_size',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='daily_drawdown',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='leverage',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='package_description',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='package_name',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='phase_description',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='price',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='total_drawdown',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='trading_platform',
        ),
        migrations.RemoveField(
            model_name='propfirm',
            name='years_of_operation',
        ),
        migrations.AddField(
            model_name='propfirm',
            name='account_plans',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='propfirm',
            name='trading_platforms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('MT4', 'MT4'), ('MT5', 'MT5'), ('CTrader', 'CTrader'), ('MatchTrader', 'MatchTrader'), ('DXTrade', 'DXTrade'), ('In-House Trading Platform', 'In-House Trading Platform')], max_length=250), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='propfirm',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
