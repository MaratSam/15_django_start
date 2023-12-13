from django.shortcuts import render


def index(request):
    return render( request, "main_app/1.html" )
    

def about(request):
    return render (request, 'main_app/about.html')
