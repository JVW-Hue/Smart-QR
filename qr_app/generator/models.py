from django.db import models
import uuid

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    color = models.CharField(max_length=7, default='#000000')
    background_color = models.CharField(max_length=7, default='#ffffff')
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    payment_intent_id = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"QR Code: {self.content[:50]}..."