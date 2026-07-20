from django.db import models

# Create your models here.
class Chatbot(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)