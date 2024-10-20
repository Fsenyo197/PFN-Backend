from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField

class DiscountCode(models.Model):
    # Fields for the discount code
    firm_name = models.CharField(max_length=250, null=False, blank=False)
    discount_code = models.CharField(max_length=100, unique=True, null=False, blank=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Percentage value (e.g., 10.00 for 10%)
    image = CloudinaryField('image', null=True, blank=True)  # Image field (optional)
    title = models.CharField(max_length=250, null=False, blank=False)  # Title of the discount
    body = HTMLField(blank=True)  # Description (rich text content)
    date = models.DateField(default=timezone.now)  # Date when the discount was added
    duration = models.PositiveIntegerField()  # Duration in days (or other units)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']  # Latest discounts first

    def __str__(self):
        return f'{self.firm_name} - {self.discount_code}'

    def is_active(self):
        """Returns True if the discount is still valid based on the duration."""
        expiry_date = self.date + timezone.timedelta(days=self.duration)
        return timezone.now().date() <= expiry_date
