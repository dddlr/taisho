from django.contrib import admin

from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pron', 'gloss', 'note')

admin.site.register(Word, WordAdmin)
