from django.db import models

class Word(models.Model):
    word = models.CharField("Chinese word or phrase", max_length=10)
    pron = models.CharField("Pronunciation", max_length=50)
    gloss = models.TextField("Gloss/definition(s)")
    note = models.CharField("Note", max_length=100, blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.word

class Category(models.Model):
    name = models.CharField("Category name", max_length=30)

    def __str__(self):
        return self.name

class Sentence(models.Model):
    sentence = models.CharField("Sentence", max_length=60)
    romanised = models.CharField("Romanised", max_length=200)
    english = models.CharField("English translation", max_length=200)
    source = models.CharField("source (d = dad, m = mum, u = me, g = grandma)", max_length=1)

    def __str__(self):
        return self.sentence
