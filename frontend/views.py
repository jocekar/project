from django.shortcuts import render
from adminfolder import *
from adminfolder.models import *
# Create your views here.

def frontend(request):
     home = Home.objects.first()
     about = About.objects.first()
     image = Iamge.objects.all()
     skills = Skill.objects.all()
     musics = Music.objects.all()
     context ={
     "home":home,
     'about':about,
     'image':image,
     'skills':skills,
     'musics':musics
    }
     return render(request,'pages/index.html',context)

def portfolio_detail(request,pk):
     return render(request, 'pages/portfolio-details.html')