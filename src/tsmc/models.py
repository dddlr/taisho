from django.db import models

class Character(models.Model):
    char = models.CharField("Chinese character", max_length=1)
    initial = models.CharField(
        "initial consonant in Middle Chinese",
        max_length=1
    )
    final = models.CharField("final in Middle Chinese", max_length=1)
    tone = models.CharField("tone in Middle Chinese", max_length=1)
    openness = models.CharField("openness in Middle Chinese (1 = open, 2 = closed)", max_length=1)
    division = models.IntegerField("division in Middle Chinese")
    note = models.CharField("note on character", max_length=10, blank=True)

    def division_chinese(self):
        divisions = ['一', '二', '三', '四']
        return divisions[self.division - 1]

    def __str__(self):
        return self.char + '（' + self.initial + self.final + self.tone + \
        self.openness + self.division_chinese() + '）'

class Taishanese(models.Model):
    char = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        verbose_name="Chinese character"
    )
    initial = models.CharField("initial consonant in Taishanese", max_length=3, blank=True)
    final = models.CharField("final in Taishanese", max_length=4)
    tone = models.CharField("tone in Taishanese", max_length=3)

    def __str__(self):
        return self.initial + self.final + self.tone

    def test(self):
        return len(self.final)
