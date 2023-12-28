from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


# Create your views here.
def news_home (request):
    news = Articles.objects.all()
    return render(request,'news_home.html', {'news':news})

def create (request):
    error=''
    if request.method == 'POST':
        form=ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='The form was filled in incorrectly'

    form=ArticlesForm()
    data= {
        'form':form
    }
    return render(request,'create.html', data)