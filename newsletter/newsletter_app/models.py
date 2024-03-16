from django.db import models


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)


class Newsletter(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
