from django.db import models
from django.db.models import JSONField
from django.utils import timezone
from django.utils.text import slugify

class PropFirm(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    # Basic Prop Firm Fields
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=False, blank=True)
    about = models.TextField(blank=True)
    website = models.URLField(null=True, blank=True, unique=True)
    year_established = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    firm_type = models.CharField(max_length=100, blank=True)
    drawdown_type = models.CharField(max_length=100, blank=True)
    payout_frequency = models.CharField(max_length=100, blank=True)

    # Features
    copy_trading_rule = models.BooleanField(default=False)
    consistency_rule = models.BooleanField(default=False)
    two_percent_rule = models.BooleanField(default=False)
    stop_loss_rule = models.BooleanField(default=False)
    vpn_and_vps_rule = models.BooleanField(default=False)
    weekend_holding_rule = models.BooleanField(default=False)
    countries_prohibited = models.TextField(blank=True)

    # Choices for payout and payment options
    PAYOUT_OPTIONS_CHOICES = [
        ('Bank Transfer', 'Bank Transfer'),
        ('Rise', 'Rise'),
        ('Direct Crypto', 'Direct Crypto'),
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
        ('Astropay', 'Astropay'),
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
        ('TradeLocker', 'TradeLocker'),
        ('Trading View', 'Trading View'),
        ('In-House Trading Platform', 'In-House Trading Platform'),
    ]

    trading_platforms = JSONField(
        models.CharField(max_length=250, choices=TRADING_PLATFORMS_CHOICES),
        blank=True,
        default=list,
    )

    # New fields with indexing
    is_active = models.BooleanField(default=True, db_index=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', db_index=True)
    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now, db_index=True)
    date_created = models.DateTimeField(default=timezone.now, db_index=True)
    date_updated = models.DateTimeField(auto_now=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate initial slug
            self.slug = slugify(self.name, allow_unicode=True).replace('-', '_')
            original_slug = self.slug

            # Ensure uniqueness by appending a counter if needed
            queryset = PropFirm.objects.filter(slug=original_slug).exclude(pk=self.pk)
            counter = 1
            while queryset.exists():
                self.slug = f'{original_slug}_{counter}'
                counter += 1

        super().save(*args, **kwargs)

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

    ACCOUNT_TYPE_CHOICES = [
        ('Forex', 'Forex'),
        ('Stocks', 'Stocks'),
        ('Crypto', 'Crypto'),
        ('Futures', 'Futures'),
    ]

    # ForeignKey relationship with PropFirm (automatically indexed)
    prop_firm = models.ForeignKey(
        PropFirm, related_name="account_plans", on_delete=models.CASCADE
    )
    phase = models.CharField(max_length=50, default="two_phase", choices=PHASE_CHOICES, db_index=True)
    account_type = models.CharField(max_length=50, default="Forex", choices=ACCOUNT_TYPE_CHOICES)
    account_size = models.CharField(max_length=50, db_index=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, db_index=True)
    profit_split_ratio = models.CharField(max_length=50, default="0")
    leverage = models.CharField(max_length=50, default="0")
    minimum_trading_days = models.CharField(max_length=50, default="0")
    profit_target = models.CharField(max_length=50, default="0")
    phase_time_limit = models.CharField(max_length=50, default="0")
    daily_drawdown = models.CharField(max_length=10, default="0")
    total_drawdown = models.CharField(max_length=10, default="0")

    # New fields
    currency = models.CharField(max_length=10, default="USD")
    is_available = models.BooleanField(default=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', db_index=True)

    def __str__(self):
        return f"{self.phase} - {self.account_size}"
