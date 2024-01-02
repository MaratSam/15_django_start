from django.shortcuts import render


def index(request):
    data = {"title123":"!",
    "my_values" : ['1', "2", "3" ],
    'obj':{'car':'BMW',
           "age" : 33,
           "hobby" :"football"}}

    return render( request, "main_app/1.html", data )
    

def about(request):
    return render (request, 'main_app/about.html')
