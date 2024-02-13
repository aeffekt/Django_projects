from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=200)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_done = models.DateTimeField(auto_now=True)
    done_status = models.BooleanField(default=False)

    def make_done(self):
        self.done_status=True

    def __str__(self):        
        return self.title
    
    class Meta:
        ordering=['done_status']
