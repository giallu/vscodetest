from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=128)
    sound = models.CharField(max_length=128)

    def speak(self):
        return 'The {} says "{}"'.format(self.name, self.sound)