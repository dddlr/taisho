from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Word

def search(request):
    """Render search and results page of Taishanese dictionary."""
    word_list = Word.objects.all().filter(public=True).order_by('word')
    paginator = Paginator(word_list, 20)

    page = request.GET.get('page', 1)
    words = None
    try:
        words = paginator.get_page(page)
    except InvalidPage:
        return render() # TODO

    context = { 'results': words }

    # TODO: search function
    VALID_COLUMNS = ['word', 'pron', 'gloss']

    return render(request, 'tspron/index.html', context)

def about(request):
    """Return about page."""
    return render(request, 'tspron/about.html')
