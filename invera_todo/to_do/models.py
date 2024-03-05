from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created =models.DateTimeField(auto_now_add=True)
    done_status = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class META:
        ordering = ['done_status', 'created']

    def __str__(self):
        return self.title