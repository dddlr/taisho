from django.db import models

# Unfinished

class Word(models.Model):
    word = models.CharField("Chinese word or phrase", max_length=10)
    pron = models.CharField("Pronunciation", max_length=30)
    gloss = models.CharField("Gloss", max_length=50)
    note = models.CharField("Note", max_length=100, blank=True)

    def __str__(self):
        return self.word
