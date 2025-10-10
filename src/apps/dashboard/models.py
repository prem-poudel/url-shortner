from django.db import models
from django.db.models import F
from src.apps.auth.models import User
from .utils import convert_to_base62


class ShortLink(models.Model):
    id: int
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.PositiveIntegerField(default=0)

    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # Only generate short_code if new and not set
        if is_new and not self.short_code:
            self.short_code = convert_to_base62(self.id)
            ShortLink.objects.filter(id=self.id).update(short_code=self.short_code)
            self.refresh_from_db(fields=['short_code'])

    def increment_clicks(self):
        """Increase click count atomically (only when user visits)."""
        ShortLink.objects.filter(pk=self.pk).update(clicks=F('clicks') + 1)
        self.refresh_from_db(fields=['clicks'])

    @classmethod
    def create_short_link(cls, user, original_url):
        """Create a new short link and ensure short_code is generated."""
        link = cls.objects.create(user=user, original_url=original_url)
        link.refresh_from_db(fields=['short_code'])
        return link

    def __str__(self):
        return f"{self.short_code} → {self.original_url} ({self.clicks} clicks)"
