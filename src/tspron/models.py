from django.db import models

# Unfinished

class Word(models.Model):
    char = models.CharField("Chinese word or phrase", max_length=10)

    def __str__(self):
        return self.char

