from django.db import models

# Create your models here.


class banner(models.Model):

    image1 = models.ImageField(upload_to='uploads')
   