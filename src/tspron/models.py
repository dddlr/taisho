from django.db import models

# Unfinished

class Word(models.Model):
    word = models.CharField("Chinese word or phrase", max_length=10)
    pron = models.CharField("Pronunciation", max_length=30)
    gloss = models.CharField("Gloss", max_length=100)
    note = models.CharField("Note", max_length=100, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.word

class Category(models.Model):
    name = models.CharField("Category name", max_length=30)

    def __str__(self):
        return self.name

# class Sentence(models.Model):
    # pass
