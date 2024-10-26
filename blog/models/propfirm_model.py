from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField  

class PropFirm(models.Model):
    # Prop Firm Fields
    name = models.CharField(max_length=250, null=False, blank=False, unique=True)
    about = models.TextField(blank=True)  # Detailed description about the prop firm
    news_rule = models.BooleanField(default=False)
    copy_trading = models.BooleanField(default=False)
    consistency_rule = models.BooleanField(default=False)
    countries_prohibited = models.TextField(blank=True)
    crypto_payout_option = models.BooleanField(default=False)

    # Using JSONField to store account plans as a list of dictionaries
    account_plans = JSONField(blank=True, default=list)

    # Trading platforms field using ArrayField for PostgreSQL
    TRADING_PLATFORMS_CHOICES = [
        ('MT4', 'MT4'),
        ('MT5', 'MT5'),
        ('CTrader', 'CTrader'),
        ('MatchTrader', 'MatchTrader'),
        ('DXTrade', 'DXTrade'),
        ('In-House Trading Platform', 'In-House Trading Platform')
    ]

    trading_platforms = ArrayField(
        models.CharField(max_length=250, choices=TRADING_PLATFORMS_CHOICES),
        blank=True,
        default=list,
    )

    PHASE_CHOICES = [
        ('one_phase', 'One Phase'),
        ('two_phase', 'Two Phase'),
        ('three_phase', 'Three Phase'),
        ('four_phase', 'Four Phase'),
        ('instant_funding', 'Instant Funding'),
    ]
