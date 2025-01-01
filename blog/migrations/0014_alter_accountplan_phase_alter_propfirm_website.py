# Generated by Django 5.1 on 2025-01-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_accountplan_phase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountplan',
            name='phase',
            field=models.CharField(choices=[('one_phase', 'One Phase'), ('two_phase', 'Two Phase'), ('three_phase', 'Three Phase'), ('four_phase', 'Four Phase'), ('instant_funding', 'Instant Funding')], default='two_phase', max_length=50),
        ),
        migrations.AlterField(
            model_name='propfirm',
            name='website',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]