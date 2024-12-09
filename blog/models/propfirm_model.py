from django.db import models
from django.db.models import JSONField

class PropFirm(models.Model):
    # Basic Prop Firm Fields
    name = models.CharField(max_length=250, unique=True)
    about = models.TextField(blank=True) 
    year_established = models.PositiveIntegerField(null=True, blank=True)
    location = models.TextField(blank=True)
    firm_type = models.CharField(max_length=100, blank=True)

    # Features
    news_rule = models.BooleanField(default=False)
    copy_trading = models.BooleanField(default=False)
    consistency_rule = models.BooleanField(default=False)
    two_percent_rule = models.BooleanField(default=False)
    countries_prohibited = models.TextField(blank=True)
    
    # Options
    payout_options = models.CharField(max_length=250, blank=True)
    payment_options = models.CharField(max_length=250, blank=True) 

    # Account plans as a list of dictionaries
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

    trading_platforms = JSONField(
        models.CharField(max_length=250, choices=TRADING_PLATFORMS_CHOICES),
        blank=True,
        default=list,
    )
