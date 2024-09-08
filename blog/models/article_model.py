from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from blog.utils.blog_utils import count_words, read_time
from blog.models.category_model import Category
import cloudinary.uploader
import environ

# Initialize environment variables
env = environ.Env()

class ArticleManager(models.Manager):
    def get_queryset(self):
        # Override default to exclude 'deleted' articles
        return super().get_queryset().filter(deleted=False)

    def deleted(self):
        # Custom queryset for retrieving only deleted articles
        return super().get_queryset().filter(deleted=True)

class Article(models.Model):
    # Article status constants
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
    image = models.ImageField(null=True, blank=True)  # Removed `upload_to='articles/'`
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

        # Upload image to Cloudinary if a new image is provided
        if self.image and self._state.adding:  # Upload image when creating a new instance
            upload_response = cloudinary.uploader.upload(self.image)
            self.image = upload_response.get('secure_url')

        # Handle word count and read time
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
