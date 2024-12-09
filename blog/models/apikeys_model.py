from django.db import models
from django.contrib.auth.models import User
import secrets

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="api_keys")
    key = models.CharField(max_length=40, unique=True)
    secret = models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_hex(20)
        if not self.secret:
            self.secret = secrets.token_hex(20)
        super().save(*args, **kwargs)

    def revoke(self):
        self.is_active = False
        self.save()

    def __str__(self):
        status = "Active" if self.is_active else "Revoked"
        return f"{self.user.username} - {status} (Created: {self.created_at})"

    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"