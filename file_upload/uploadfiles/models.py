from django.db import models

class ls_20(models.Model):
    Elect_file = models.FileField(upload_to='election/')
    # def __str__(self):
    #     return self.Elect_file

# Create your models here.
