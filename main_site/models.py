from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class BookAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_appointments")
    doc_name = models.CharField(max_length=50)
    app_date = models.DateField()
    timestamp = models.DateField(default=now)
    

    def __str__(self):
        return f"User: {self.user.username}, Doctor: {self.doc_name}"
    