from django.db import models

class Word(models.Model):
    word = models.CharField("Chinese word or phrase", max_length=10)
    gloss = models.TextField("Gloss/definition(s)")
    note = models.TextField("Note", blank=True)
    date = models.DateField("Date")
    # deprecated, TODO remove
    pron_old = models.CharField("Pronunciation (old)", max_length=75,
                                blank=True)
    pron_note = models.TextField("Pronunciation note", blank=True)
    public = models.BooleanField("Public?", default=False)

    def __str__(self):
        return self.word

class Pron(models.Model):
    pron = models.CharField("Pronunciation", max_length=50)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    date = models.DateField("Date")
    # d = dad, m = mum, u = me, gm = grandma
    source = models.CharField("Source", max_length=5)

    def __str__(self):
        return f"{self.pron} ({self.source}, {self.date})"

class Sentence(models.Model):
    sentence = models.CharField("Sentence", max_length=60)
    romanised = models.CharField("Romanised", max_length=200)
    english = models.CharField("English translation", max_length=200)
    source = models.CharField("source (d = dad, m = mum, u = me, gm = grandma)",
                              max_length=1)
    note = models.TextField("Note", blank=True)
    date = models.DateField("Date", null=True, blank=True)

    def __str__(self):
        return self.sentence
