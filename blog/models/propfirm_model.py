from django.db import models
from django.db.models import JSONField

class PropFirm(models.Model):
    # Basic Prop Firm Fields
    name = models.CharField(max_length=250, unique=True) 
    year_established = models.PositiveIntegerField(null=True, blank=True)
    location = models.TextField(blank=True)
    firm_type = models.CharField(max_length=100, blank=True)
    drawdown_type = models.CharField(max_length=100, blank=True)
    payout_frequency = models.CharField(max_length=100, blank=True)

    # Features
    news_rule = models.BooleanField(default=False)
    copy_trading = models.BooleanField(default=False)
    consistency_rule = models.BooleanField(default=False)
    two_percent_rule = models.BooleanField(default=False)
    stop_loss_rule = models.BooleanField(default=False)
    countries_prohibited = models.TextField(blank=True)
    
    # Choices for payout and payment options
    PAYOUT_OPTIONS_CHOICES = [
        ('Bank Transfer', 'Bank Transfer'),
        ('PayPal', 'PayPal'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('Skrill', 'Skrill'),
        ('Neteller', 'Neteller'),
    ]

    PAYMENT_OPTIONS_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('PayPal', 'PayPal'),
        ('Stripe', 'Stripe'),
    ]

    # Payout and payment options fields
    payout_options = JSONField(
        models.CharField(max_length=250, choices=PAYOUT_OPTIONS_CHOICES),
        blank=True,
        default=list,
    )
    payment_options = JSONField(
        models.CharField(max_length=250, choices=PAYMENT_OPTIONS_CHOICES),
        blank=True,
        default=list,
    )

    # Account plans as a list of dictionaries
    account_plans = JSONField(blank=True, default=list)

    # Trading platforms field using ArrayField for PostgreSQL
    TRADING_PLATFORMS_CHOICES = [
        ('MT4', 'MT4'),
        ('MT5', 'MT5'),
        ('CTrader', 'CTrader'),
        ('MatchTrader', 'MatchTrader'),
        ('DXTrade', 'DXTrade'),
        ('In-House Trading Platform', 'In-House Trading Platform'),
    ]

    trading_platforms = JSONField(
        models.CharField(max_length=250, choices=TRADING_PLATFORMS_CHOICES),
        blank=True,
        default=list,
    )
