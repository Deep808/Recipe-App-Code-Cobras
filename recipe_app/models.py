from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    createdAt = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.title} - {self.createdAt}"