from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # el user se importa xq fue creado por django
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # auto_now=True == actualiza al modificar
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # con esto le decimos a django donde encontrar la URL
    def  get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
