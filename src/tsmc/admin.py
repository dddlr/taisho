from django.contrib import admin

from .models import Character, Taishanese

class TaishaneseInline(admin.StackedInline):
    model = Taishanese
    extra = 1

class CharacterAdmin(admin.ModelAdmin):
    inlines = [TaishaneseInline]
    list_display = ('__str__', 'note', 'taishanese')
    # save_on_top = True
    search_fields = ('char',)

    def taishanese(self, obj):
        """Get the Taishanese pronunciation(s) of a character as a string."""
        return ', '.join(map(str, Taishanese.objects.filter(char=obj.id)))

class TaishaneseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'char', 'note', 'source')
    save_on_top = True
    search_fields = ('initial','final','tone','note','source',)

admin.site.register(Character, CharacterAdmin)
admin.site.register(Taishanese, TaishaneseAdmin)
