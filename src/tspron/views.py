from django.shortcuts import render

def index(request):
    return HttpResponse("Taishanese pronunciation.")

def word(request, word_id):
    response = "This is word ID %s"
    return HttpResponse(response % word_id)
