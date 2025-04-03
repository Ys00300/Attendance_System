from django.db import models
from django.conf import settings  # Import settings to reference the custom user model

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)  # Time when message was read

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.sent_at}"

    def mark_as_read(self):
        self.read_at = models.DateTimeField(auto_now=True)
        self.save()
