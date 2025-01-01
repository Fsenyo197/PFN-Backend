# Generated by Django 5.1 on 2025-01-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_accountplan_account_type_propfirm_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountplan',
            name='account_type',
            field=models.CharField(choices=[('Forex', 'Forex'), ('Stocks', 'Stocks'), ('Crypto', 'Crypto'), ('Futures', 'Futures')], default='Forex', max_length=50),
        ),
    ]
