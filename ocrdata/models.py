from django.db import models

# Create your models here.

class ocrresult(models.Model):
    image_path = models.CharField(max_length=255)
    ocr_text = models.TextField()