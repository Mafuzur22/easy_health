from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class ChatData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_messages")
    type = models.CharField(max_length=5)
    message_data = models.TextField()
    timestamp = models.DateField(default=now)
    def __str__(self):
        return self.user.username

class BookAppointment(models.Model):
    user = models.ForeignKey(on_delete=models.CASCADE, related_name="user_appointments")
    doc_name = models.CharField(max_length=50)
    