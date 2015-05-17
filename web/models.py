from django.db import models


class ContactMessage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    email = models.EmailField()
