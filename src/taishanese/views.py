from django.shortcuts import render

def home(request):
    # TODO add links to dict and tsmc
    return render(request, 'index.html')
