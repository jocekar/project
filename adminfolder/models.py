from django.db import models
from datetime import datetime
# Create your models here.

############ home ###########
class Home(models.Model):
     name = models.CharField(max_length = 20, null=True)
     nav = models.CharField(max_length = 15, null=True)
     text = models.TextField(null=True)
     image = models.ImageField(upload_to='backgroundimage', null=True)

     def __str__(self):
          return self.name

#### about
class About(models.Model):
     about = models.CharField(max_length=40, null=True)
     title = models.CharField(max_length = 50, null=True)
     birthday = models.DateField(null=True)
     website = models.CharField(max_length=50, null=True)
     phone = models.CharField(max_length=50,null=True)
     city = models.CharField(max_length=50, null=True)
     email = models.CharField(max_length = 50, null=True)
     descriptions = models.TextField(null=True)

     def __str__(self):
          return self.title

     @property
     def birthdayAge(self):
          return int((datetime.now().date()-self.birthday).days/365.25)

### my skill
class Skill(models.Model):
     skill = models.IntegerField( null=True)
     title = models.CharField(max_length=15, null=True)

     def __str__(self):
          return self.title

##### images
class Category(models.Model):
     category = models.CharField(max_length=40, null=True)

     def __str__(self):
          return self.category

class Iamge(models.Model):
     title = models.CharField(max_length = 40, null=True)
     image_date = models.DateField(null=True)
     category =models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
     text = models.TextField(null=True)
     image = models.ImageField(upload_to='backgroundimage', null=True)
     created = models.DateTimeField(auto_now_add=True, null=True)
     updated = models.DateTimeField(auto_now=True, null=True)

     def __str__(self):
          return self.title

     class Meta:
          ordering = [ '-created', '-updated' ]

##### Music
class Music(models.Model):
     title = models.CharField(max_length=40, null=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
     music = models.FileField(upload_to ='mp-4/%y')

     def __str__(self):
          return self.title

### song
class Song(models.Model):
     title = models.CharField(max_length=40, null=True)
     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
     song = models.FileField(upload_to ='song/')

     def __str__(self):
          return self.title
