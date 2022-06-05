from django.db import models

class Initial(models.Model):
    class Meta:
        ordering = ('name', 'baxter')

    name = models.CharField("Name", max_length=2)
    baxter = models.CharField("Baxter's transcription", max_length=4)
    other = models.CharField("Other initials this encompasses", max_length=4, blank=True)
    def __str__(self):
        return self.baxter + ' (' + self.name + ')'

class Final(models.Model):
    class Meta:
        ordering = ('name', 'baxter')

    name = models.CharField("Name", max_length=1)
    baxter = models.CharField("Baxter's transcription", max_length=8)

    def __str__(self):
        return self.baxter + ' (' + self.name + ')'

class Character(models.Model):
    char = models.CharField("Chinese character", max_length=2)
    # TODO: remove initial and final when entire database is done
    initial = models.CharField(
        "initial consonant in Middle Chinese",
        max_length=2
    )
    final = models.CharField("final in Middle Chinese", max_length=1)
    initial_key = models.ForeignKey("Initial", on_delete=models.SET_NULL, null=True)
    final_key = models.ForeignKey("Final", on_delete=models.SET_NULL, null=True)
    tone = models.CharField("tone in Middle Chinese", max_length=1)
    openness = models.CharField("openness in Middle Chinese (1 = open, 2 = closed)", max_length=1)
    division = models.IntegerField("division in Middle Chinese")
    note = models.CharField("existing note", max_length=50, blank=True)
    own_note = models.CharField("my own note", max_length=50, blank=True)
    variant = models.CharField("more common character", max_length=2, blank=True)
    jiyun_only = models.BooleanField("jiyun only?", default=False)
    external = models.BooleanField("from outside chengyun + jiyun?", default=False)
    # chongniu = models.BooleanField("chongniu?", default=False)
    # simplified = models.CharField("Simplified character, if any", max_length=2)

    def division_chinese(self):
        divisions = ['一', '二', '三', '四']
        return divisions[self.division - 1]

    def __str__(self):
        character = self.char
        if self.variant:
            character += '／' + self.variant

        character += '（'

        if self.initial_key:
            character += self.initial_key.name
        else:
            character += '？'
        if self.final_key:
            character += self.final_key.name
        else:
            character += '？'

        character += self.tone + self.openness + self.division_chinese()

        if self.jiyun_only:
            character += '＊'
        if self.external:
            character += '＃'

        character += '）'

        return character

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

        return self.initial_key.name + self.final_key.name + tone + openness + self.division_chinese()

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
