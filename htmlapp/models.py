from django.db import models

# Create your models here.


class Recipe(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    photo=models.ImageField(upload_to='upload/')
    created_at=models.DateTimeField(auto_now_add=True)
