from django.contrib import admin

from .models import Character, Taishanese

class TaishaneseInline(admin.StackedInline):
    model = Taishanese
    extra = 1

class CharacterAdmin(admin.ModelAdmin):
    inlines = [TaishaneseInline]
    list_display = ('__str__', 'note')
    # save_on_top = True
    search_fields = ('char',)

class TaishaneseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'char', 'note', 'source')
    save_on_top = True
    search_fields = ('initial','final','tone','note','source',)

admin.site.register(Character, CharacterAdmin)
admin.site.register(Taishanese, TaishaneseAdmin)
