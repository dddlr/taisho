from django.contrib import admin

from .models import Word, Pron, Sentence

class PronInline(admin.StackedInline):
    model = Pron
    min_num = 1
    extra = 0
    search_fields = ('__str__',)

class WordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pron_old', 'prons', 'gloss', 'note', 'date', 'public')
    inlines = [PronInline]

    def prons(self, word):
        """Get all the pronunciations of a word."""
        return ' / '.join(str(x) for x in Pron.objects.filter(word=word.id))

class PronAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'word', 'date')

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'romanised', 'english', 'source')

admin.site.register(Word, WordAdmin)
admin.site.register(Pron, PronAdmin)
admin.site.register(Sentence, SentenceAdmin)
