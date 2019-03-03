from django.db import models

class Character(models.Model):
    char = models.CharField("Chinese character", max_length=2)
    initial = models.CharField(
        "initial consonant in Middle Chinese",
        max_length=2
    )
    final = models.CharField("final in Middle Chinese", max_length=1)
    tone = models.CharField("tone in Middle Chinese", max_length=1)
    openness = models.CharField("openness in Middle Chinese (1 = open, 2 = closed)", max_length=1)
    division = models.IntegerField("division in Middle Chinese")
    note = models.CharField("existing note", max_length=50, blank=True)
    own_note = models.CharField("my own note", max_length=50, blank=True)
    variant = models.CharField("more common character", max_length=2, blank=True)
    jiyun_only = models.BooleanField("jiyun only?", default=False)
    external = models.BooleanField("from outside chengyun + jiyun?", default=False)
    # simplified = models.CharField("Simplified character, if any", max_length=2)

    def division_chinese(self):
        divisions = ['一', '二', '三', '四']
        return divisions[self.division - 1]

    def __str__(self):
        extras_start = ''
        if self.variant:
            extras_start = '／' + self.variant
        extras_end = []
        if self.jiyun_only:
            extras_end.append('＊')
        if self.external:
            extras_end.append('＃')
        return self.char + extras_start + '（' + self.initial + self.final + \
        self.tone + self.openness + self.division_chinese() + \
        ''.join(extras_end) + '）'

    def info(self):
        # Until I update the values in the database so they're not numbers
        tones = ['平', '上', '去', '入']
        opennesses = ['開', '合']
        tone = self.tone
        openness = self.openness
        try:
            tone = tones[int(self.tone) - 1]
        except ValueError:
            pass
        try:
            openness = opennesses[int(self.openness) - 1]
        except ValueError:
            pass

        return self.initial + self.final + tone + openness + self.division_chinese()

class Taishanese(models.Model):
    char = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        verbose_name="Chinese character"
    )
    initial = models.CharField("initial consonant in Taishanese", max_length=3, blank=True)
    final = models.CharField("final in Taishanese", max_length=4)
    tone = models.CharField("tone in Taishanese", max_length=3)
    note = models.CharField("note", max_length=50, blank=True)
    source = models.CharField("source (d = dad, m = mum, u = me but unverified, g = grandma)", max_length=1)
    date = models.DateField("date", blank=True, null=True)

    def __str__(self):
        return self.initial + self.final + self.tone + ' (' + self.source + ')'

    def syllable(self):
        return self.initial + self.final

    def test(self):
        return len(self.final)
