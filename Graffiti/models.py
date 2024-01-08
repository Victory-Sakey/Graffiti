from django.db import models

# Create your models here.
class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class JoinCommunitySubmission(models.Model):
    name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=100)
    email = models.EmailField()