from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=20)
    descrip = models.TextField()
    stat = models.BooleanField()
