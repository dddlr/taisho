from django.contrib import admin

from .models import Initial, Final, Character, Taishanese

class InitialAdmin(admin.ModelAdmin):
    search_fields = ('name','baxter')

class FinalAdmin(admin.ModelAdmin):
    search_fields = ('name','baxter')

class TaishaneseInline(admin.StackedInline):
    model = Taishanese
    extra = 1
    search_fields = ('__str__',)

class CharacterAdmin(admin.ModelAdmin):
    inlines = [TaishaneseInline]
    list_display = ('__str__', 'note', 'taishanese')
    # save_on_top = True
    search_fields = ('char',)
    autocomplete_fields = ('initial_key', 'final_key')
    exclude = ('initial', 'final')

    def taishanese(self, obj):
        """Get the Taishanese pronunciation(s) of a character as a string."""
        return ', '.join(map(str, Taishanese.objects.filter(char=obj.id)))

class TaishaneseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'char', 'note', 'source')
    # save_on_top = True
    search_fields = ('initial','final','tone','note','source',)
    # speed up page loading by loading character as just an ID
    raw_id_fields = ('char',)

admin.site.register(Initial, InitialAdmin)
admin.site.register(Final, FinalAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Taishanese, TaishaneseAdmin)
