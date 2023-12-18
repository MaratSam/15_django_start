from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    brief_desription = models.CharField('Brief Description (Anons)', max_length=250)
    full_text = models.TextField("Article's text")
    date = models.DateTimeField("Article's date")

    def __str__(self):
        return f'The news: {self.title}'
    
    class Meta:
        verbose_name = "News table"
        verbose_name_plural = "News tables"
