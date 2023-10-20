from django.db import models

# Create your models here.

class MyFileUpload(models.Model):
    file_name=models.CharField(max_length=54)
    my_file=models.FileField()