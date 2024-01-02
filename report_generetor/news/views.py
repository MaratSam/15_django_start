from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from datetime import datetime


# Create your views here.
def news_home (request):
    news = Articles.objects.order_by('-date')
    return render(request,'news/news_home.html', {'news':news})

class NewsDetailView (DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView (UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
   
class NewsDeleteView (DeleteView):
    model = Articles
    success_url = "/news/"
    template_name = 'news/news-delete.html'
    

def create (request):
    error=''
    if request.method == 'POST': #we process the returning data in the same this function
        form=ArticlesForm(request.POST)
        
        if form.is_valid():
            entry=form.save(commit=False)   # commit=False tells Django that "Don't send this to database yet; there are more things I want to do with it."
            entry.date=datetime.now()
            entry.save() # Now you can send it to DB
            return redirect('news_home')
        else:
            error='The form was filled in incorrectly'

    form=ArticlesForm()
    data= {
        'form':form,
        'error':error
    }
    return render(request,'news/create.html', data)