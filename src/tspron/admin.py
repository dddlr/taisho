from django.contrib import admin

from .models import Category, Word, Sentence

class WordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pron', 'gloss', 'note', 'date')

class CategoryAdmin(admin.ModelAdmin):
    pass

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'romanised', 'english', 'source')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Sentence, SentenceAdmin)
