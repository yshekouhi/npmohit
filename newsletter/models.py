from django.db import models
import uuid

class Subscriber(models.Model):
    email = models.EmailField(("ایمیل"), unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(("تایید شده؟"), default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'اشتراک خبرنامه'
        verbose_name_plural = 'اشتراک خبرنامه'   

    def __str__(self):
        return self.email           

