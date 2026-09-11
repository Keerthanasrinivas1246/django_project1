from django import forms 
from .models import Article,Genre

class GenreForm(forms.ModelForm):
    class Meta: # it will display the input tag
        model=Genre
        fields = ['name','desc','rating']

    # class Meta:
    #     model=Genre
    #     exclude = ['created_at']

class ArticleForm(forms.ModelForm): # model form created
    class Meta: # it will display the input tag
        model=Article
        fields = ['type','title','summary','author_name','tags','image','video'] # optional--> fields ='__all__'

    # class Meta:
    #     model=Article
    #     exclude = ['created_at']
