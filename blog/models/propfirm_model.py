from django.db import models
from django.db.models import JSONField
from django.utils import timezone

class PropFirm(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    # Basic Prop Firm Fields
    name = models.CharField(max_length=250, unique=True) 
    website = models.URLField(null=True, blank=True)
    year_established = models.CharField(max_length=100, null=True, blank=True)
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
        ('Rise', 'Rise'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('Wise', 'Wise'),
    ]

    PAYMENT_OPTIONS_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cryptocurrency', 'Cryptocurrency'),
        ('PayPal', 'PayPal'),
        ('Koka', 'Koka'),
        ('Skrill', 'Skrill'),
        ('Neteller', 'Neteller'),
        ('Google Pay', 'Google Pay'),
        ('Apple Pay', 'Apple Pay'),
        ('Payoneer', 'Payoneer'),
        ('Paysafe Card', 'Paysafe Card'),
        ('Wise', 'Wise'),
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

    # New fields
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AccountPlan(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    PHASE_CHOICES = [
        ('one_phase', 'One Phase'),
        ('two_phase', 'Two Phase'),
        ('three_phase', 'Three Phase'),
        ('four_phase', 'Four Phase'),
        ('instant_funding', 'Instant Funding'),
    ]

    prop_firm = models.ForeignKey(
        PropFirm, related_name="account_plans", on_delete=models.CASCADE
    )
    phase = models.CharField(max_length=50, choices=PHASE_CHOICES)
    account_size = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_split_ratio = models.CharField(max_length=50)
    daily_drawdown = models.CharField(max_length=50)
    total_drawdown = models.CharField(max_length=50)

    # New fields
    currency = models.CharField(max_length=10, default="USD")
    is_available = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.phase} - {self.account_size}"