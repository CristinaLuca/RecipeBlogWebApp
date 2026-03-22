from django import forms
from .models import Tag


class TagForm(forms.ModelForm):


    #the ModelForm provides the ability to create and update an object
    #ModelForm allows for Tag model fields to be mapped to form fields
    class Meta:
        model = Tag
        fields = ["tagName", "slug"] #tells ModelForm which model fields to use in the form
        
    #the tagName has to be all lowercase
    def clean_tagName(self):
        tag = self.cleaned_data['tagName']
        return tag.lower().strip()
  
 

class TagFormManual(forms.Form):
    tagName = forms.CharField(
        label = 'Tag Name',
        max_length = 30
        )
    slug = forms.SlugField(
        label = 'Slug name',
        max_length = 30,
        help_text = 'A label for URL config'
        )
