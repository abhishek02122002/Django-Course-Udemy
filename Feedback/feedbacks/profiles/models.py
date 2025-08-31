from django.db import models

# Create your models here.
class userProfileModel(models.Model):
     image = models.FileField(upload_to="images")