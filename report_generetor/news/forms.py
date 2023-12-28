from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields= ['title','brief_desription','full_text','date']

        widgets = {
            'title':TextInput (attrs={
                'class':'form-control',
                'placeholder':'The name of the article'
            }),
            'brief_desription' : TextInput (attrs={
                'class':'form-control',
                'placeholder':'Brief description'
            }),
            'date' : DateTimeInput (attrs={
                'class':'form-control',
                'placeholder':'Date of the article'
            }),
            'full_text' : Textarea (attrs={
                'class':'form-control',
                'placeholder':'The article itself'
            })                         
        }