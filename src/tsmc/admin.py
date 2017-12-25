from django.contrib import admin

from .models import Character, Taishanese

class TaishaneseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'char')

admin.site.register(Character)
admin.site.register(Taishanese, TaishaneseAdmin)
