from django import forms
from django.forms import fields, widgets
from blogApp.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_title', 'blog_author', 'blog_date', 'blog_read_time', 'blog_tag', 'blog_content')

        widgets ={
            'blog_title': forms.TextInput(attrs={'class':'form-control'}),
            'blog_author': forms.TextInput(attrs={'class':'form-control', 'id':'username','value':"", 'type':'hidden'}),
            #'blog_author': forms.Select(attrs={'class':'form-control'}),
            'blog_date': forms.DateInput(attrs={'class':'form-control'}),
            'blog_read_time': forms.NumberInput(attrs={'class':'form-control'}),
            'blog_tag': forms.TextInput(attrs={'class':'form-control'}),
            'blog_content': forms.Textarea(attrs={'class':'form-control'})
        }