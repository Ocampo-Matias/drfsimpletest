from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    technology=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
