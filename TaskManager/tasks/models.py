from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'Hig'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='meduim')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title



