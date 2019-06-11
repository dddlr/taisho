from django.contrib import admin

from .models import Word, Sentence

class WordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pron_old', 'gloss', 'note', 'date')

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'romanised', 'english', 'source')

admin.site.register(Word, WordAdmin)
admin.site.register(Sentence, SentenceAdmin)
