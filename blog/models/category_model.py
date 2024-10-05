from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True)
    approved = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name'),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure slug uniqueness by appending numbers if necessary
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
            original_slug = self.slug
            queryset = Category.objects.filter(slug=original_slug).exclude(pk=self.pk)
            counter = 1
            while queryset.exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1
        super(Category, self).save(*args, **kwargs)
