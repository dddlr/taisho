# from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Character, Taishanese

class CharacterView(generic.DetailView):
    model = Character
    template_name = 'tsmc/character.html'

def search(request):
    page = request.GET.get('page', 1)

    VALID_COLUMNS = ['char', 'initial', 'final', 'tone', 'openness', 'division', 'note']
    # Filter out invalid query strings from user
    columns = {column: request.GET.get(column, '') for column in VALID_COLUMNS}

    char_q_objects = Q()
    kwargs = {}

    for (key, value) in columns.items():
        if key == 'char':
            for entry in list(value):
                char_q_objects.add(Q(char=entry), Q.OR)
        else:
            kwargs[key + '__icontains'] = value

    # Filter using the character field first
    # 中文 will match 中 and 文
    queryset1 = Character.objects.filter(char_q_objects)

    # Filter using the other fields
    queryset2 = queryset1.filter(**kwargs)

    # Paginator
    paginator = Paginator(queryset2, 20)

    # Path used at the start of "Previous page"/"Next page" links
    paginator_path = request.GET.copy()
    if paginator_path.get('page', False):
        del paginator_path['page']
    paginator_path = '?' + paginator_path.urlencode() + '&'

    # The characters the paginator spurts out
    content = paginator.page(page)

    context = {'character_list': content, 'length': len(queryset2), 'paginator_path': paginator_path}
    return render(request, 'tsmc/index.html', context)
