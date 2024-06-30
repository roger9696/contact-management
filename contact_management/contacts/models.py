from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(blank=True, null=True)
  phone_number = models.CharField(max_length=15, blank=False)
  address = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name
