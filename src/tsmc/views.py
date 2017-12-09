# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Character, Taishanese

class IndexView(generic.ListView):
    template_name = 'tsmc/index.html'
    context_object_name = 'character_list'

    def get_queryset(self):
        """Return ten arbitrarily-chosen characters."""
        return Character.objects.all()[:25]

class CharacterView(generic.DetailView):
    model = Character
    template_name = 'tsmc/character.html'
