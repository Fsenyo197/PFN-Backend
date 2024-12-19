from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return now() > self.created_at + timezone.timedelta(minutes=10)
