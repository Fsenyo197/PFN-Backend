from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

class DiscountCode(models.Model):
    # Discount status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    # Fields for the discount code
    firm_name = models.CharField(max_length=250, null=False, blank=False)
    discount_code = models.CharField(max_length=100, unique=True, null=False, blank=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    image = CloudinaryField('image', null=True, blank=True)
    image_credit = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=250, null=False, blank=False)
    body = HTMLField(blank=True)
    date = models.DateField(default=timezone.now)
    duration = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFTED)
   
    # SEO Fields
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=250, blank=True, null=True)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.firm_name} - {self.discount_code}'

    def is_active(self):
        """Returns True if the discount is still valid based on the duration."""
        expiry_date = self.date + timezone.timedelta(days=self.duration)
        return timezone.now().date() <= expiry_date

    def publish(self):
        """Set the status to published."""
        self.status = self.PUBLISHED
        self.save()

    def draft(self):
        """Set the status to drafted."""
        self.status = self.DRAFTED
        self.save()
