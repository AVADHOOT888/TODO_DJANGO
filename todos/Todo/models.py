from django.db import models

# Create your models here.
class Todo(models.Model):
    text=models.CharField(max_length=300)
    created_at=models.DateTimeField()
    
    def __str__(self):
        return self.text


