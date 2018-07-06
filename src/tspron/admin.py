from django.contrib import admin

from .models import Category, Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pron', 'gloss', 'note', 'category')

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
