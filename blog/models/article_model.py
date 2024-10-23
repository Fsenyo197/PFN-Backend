from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from blog.utils.blog_utils import count_words, read_time
from blog.models.category_model import Category
from cloudinary.models import CloudinaryField

class ArticleManager(models.Manager):
    def get_queryset(self):
        # Override default to exclude 'deleted' articles
        return super().get_queryset().filter(deleted=False)

    def deleted(self):
        # Custom queryset for retrieving only deleted articles
        return super().get_queryset().filter(deleted=True)

class Article(models.Model):
    # Article and discount status constants
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )

    # BLOG MODEL FIELDS
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(unique=True)
    image = CloudinaryField('image', null=True, blank=True) 
    image_credit = models.CharField(max_length=250, null=True, blank=True)
    body = HTMLField(blank=True)
    tags = TaggableManager(blank=True)
    date_published = models.DateTimeField(null=True, blank=True, default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFTED)
    views = models.PositiveIntegerField(default=0)
    count_words = models.PositiveIntegerField(default=0)
    read_time = models.PositiveIntegerField(default=0)
    deleted = models.BooleanField(default=False)  # Soft deletion flag

    # Discount-specific fields
    firm_name = models.CharField(max_length=250, null=True, blank=True)  # Optional for non-discount articles
    discount_code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)  # Discount duration
    date = models.DateField(default=timezone.now)  # Date for both articles and discounts
    website_domain = models.URLField(max_length=255, null=True, blank=True)  # New field for storing website domain

    # SEO Fields
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    meta_keywords = models.CharField(max_length=250, blank=True, null=True)

    # Assigning custom manager
    objects = ArticleManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title')
        ]
        ordering = ('-date_published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Ensure slug uniqueness by checking if a slug exists for a different article
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
            original_slug = self.slug
            queryset = Article.objects.filter(slug=original_slug).exclude(pk=self.pk)
            counter = 1
            while queryset.exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1

        # Handle empty body
        self.count_words = count_words(self.body) if self.body else 0
        self.read_time = read_time(self.body) if self.body else 0

        super(Article, self).save(*args, **kwargs)

    def soft_delete(self):
        """Soft delete the article by setting the deleted flag to True."""
        self.deleted = True
        self.save()

    def restore(self):
        """Restore a soft-deleted article by setting the deleted flag to False."""
        self.deleted = False
        self.save()

    def is_discount_active(self):
        """Returns True if the discount is still valid based on the duration."""
        if self.duration:
            expiry_date = self.date + timezone.timedelta(days=self.duration)
            return timezone.now().date() <= expiry_date
        return False

    def publish(self):
        """Set the status to published."""
        self.status = self.PUBLISHED
        self.save()

    def draft(self):
        """Set the status to drafted."""
        self.status = self.DRAFTED
        self.save()
