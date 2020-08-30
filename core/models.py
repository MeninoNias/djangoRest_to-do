from django.db import models

# Create your models here.


class Task(models.Model):

    title = models.CharField(max_length=200)
    completd = models.BooleanField(default=False, blank=True, null=True)

    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE, null=True)
    highlighted = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.owner is not None:
            return str(self.pk) + " - " + self.owner.username + " | " +self.title
        return str(self.pk) + " - USUARIO |" +self.title