from django.db import models
from django.utils import timezone

class Item(models.Model):
    title=models.CharField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now)
    date_done = models.DateTimeField(auto_now=True)
    done_status = models.BooleanField(default=False)

    def make_done(self):
        self.done_status=True

    def __str__(self):
        if self.done_status:
            return f'{self.title}-Done'
        return f'{self.title}-To do'
