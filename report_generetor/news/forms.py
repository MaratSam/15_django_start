from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields= ['title','brief_desription','full_text']

        widgets = {
            'title':TextInput (attrs={
                'class':'form-control',
                'placeholder':'The name of the article'
            }),
            'brief_desription' : TextInput (attrs={
                'class':'form-control',
                'placeholder':'Brief description'
            }),
            'full_text' : Textarea (attrs={
                'class':'form-control',
                'placeholder':'The article itself'
            })                         
        }