from django.db import models

class Main(models.Model):
    name = models.CharField(max_length=150)
    time_cre = models.DateTimeField('Created', auto_now_add=True)
    time_upd = models.DateTimeField('Updated', auto_now=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
