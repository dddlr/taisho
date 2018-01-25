from django.db import models

# Unfinished

class Word(models.Model):
    word = models.CharField("Chinese word or phrase", max_length=10)
    pron = models.CharField("Pronunciation", max_length=20)
    gloss = models.CharField("Gloss", max_length=50)

    def __str__(self):
        return self.word
