from django.forms import ModelForm
from .models import *
from django import forms

class HomeForm(ModelForm):
     class Meta:
          model = Home 
          fields = '__all__'
          labels = {
               'name':'Name',
               'nav':'Navbar',
               'text':'Text',
               'image':'Image'
          }
          ## placeholder
          widgets ={
               'name':forms.TextInput(attrs=({'placeholder':'Enter your name...','class':'form-control'})),
               'nav':forms.TextInput(attrs=({'placeholder':'Enter your navbar...','class':'form-control'})),
               'text':forms.TextInput(attrs=({'placeholder':'Enter your text...','class':'form-control'})),
               'image':forms.FileInput(attrs=({'class':'form-control'}))
          }

#### about
class AboutForm(ModelForm):
     class Meta:
          model  = About
          fields = '__all__'
          labels ={
               'about':'About',
               'title':'Title',
               'birthday':'Birthday',
               'website':'Website',
               'phone':'Phone',
               'city':'City',
               'email':'Email',
               'descriptions':'Descriptions'
          }

          #### placeholder
          widgets = {
               'about':forms.TextInput(attrs=({'placeholder':'enter you about...','class':'form-control'})),
               'title':forms.TextInput(attrs=({'placeholder':'enter you title...','class':'form-control'})),
               'birthday':forms.DateInput(attrs=({'placeholder':'enter you about...','type':'date','class':'form-control'})),
               'website':forms.TextInput(attrs=({'placeholder':'enter you about...','class':'form-control'})),
               'phone':forms.TextInput(attrs=({'placeholder':'enter you phone...','class':'form-control'})),
               'city':forms.TextInput(attrs=({'placeholder':'enter you city...','class':'form-control'})),
               'email':forms.TextInput(attrs=({'placeholder':'enter you email...','class':'form-control'})),
               'descriptions':forms.Textarea(attrs=({'placeholder':'enter you descriptions...','class':'form-control'})),

          }

#### skill
class SkillForm(ModelForm):
     class Meta:
          model = Skill
          fields = '__all__'
          labels = {
               'title':'Title',
               'skill':"Skill"
                         }
          ### palceholder
          widgets = {
               'title':forms.TextInput(attrs=({'class':'form-control','placeholder':'enter your title ...'})),
               'skill':forms.NumberInput(attrs=({'placeholder':'enter your skill ...','class':'form-control'}))
          }

### category
class CategoryForm(ModelForm):
     class Meta:
          model = Category
          fields = '__all__'
          labels = {'category':'category'}
          ##placeholder
          widgets = {
               'category':forms.TextInput(attrs=({'placeholder':'enter write your category ...','class':'form-control'}))
          }

#### class ImageForm(ModleForm):
class ImageForm(ModelForm):
     class Meta:
          model = Iamge
          fields = '__all__'
          labels = {
               'title':'Title',
               'image_date':'Image-Date',
               'category':'Category',
               'text':'Text',
               'image':'Image'
          }

     ##### placeholder
          widgets = {
                'title':forms.TextInput(attrs=({'placeholder':'enter your title ...','class':'form-control'})),
                'image_date':forms.DateInput(attrs=({'type':'date','class':'form-control'})),
                'category':forms.Select(attrs=({'class':'form-control'})),
                'text':forms.Textarea(attrs=({'placeholder':'enter your text ...','class':'form-control'})),
                'image':forms.FileInput(attrs=({'class':'form-control'}))
          }

     def __init__(self,*args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'category...'

#### music
class MusicForm(ModelForm):
     class Meta:
          model = Music
          fields = '__all__'
          labels = {
               'title':'Title',
               'category':'Category',
               'music':'Music'
          }

          ### pkaceholder
          widgets= {
               'title':forms.TextInput(attrs=({'placeholder':'enter your title'})),
               'category':forms.Select(attrs=({'class':'form-control'})),
               'music':forms.FileInput(attrs=({'class':'form-control'}))
          }

     def __init__(self,*args, **kwargs):
        super(MusicForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'category...'