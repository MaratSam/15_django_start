from django.shortcuts import render


def index(request):
    data = {"title123":"Data from request",
    "my_values" : ['one', "two", "three" ],
    'obj':{'car':'BMW',
           "age" : 33,
           "hobby" :"football"}}

    return render( request, "main_app/1.html", data )
    

def about(request):
    return render (request, 'main_app/about.html')
