from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def backend(request):
     page = 'create'
     homes = Home.objects.all()
     form = HomeForm()
     if request.method == 'POST':
          name = request.POST.get('name')
          form =HomeForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, "' {}',  your create successfully".format(name))  # ignored
               return redirect('homepage')

     context ={
          'form':form,
          'homes':homes,
          'page':page,
     }
     return render(request, 'layout/index.html', context)

### backend-edit
def backend_edit(request, pk):
     page = 'edit'
     homes = Home.objects.all()
     home = Home.objects.get( id=pk )
     form = HomeForm(instance=home)
     if request.method == 'POST':
          form = HomeForm(request.POST,request.FILES,instance=home)
          if form.is_valid():
               form.save()
               messages.success(request, "'{}', your update successfully".format(request.POST.get('name')))
               return redirect('homepage')
     
     context = {
          'form':form,
          'home':home,
          'homes':homes
     }
     return render(request, 'layout/index.html', context)

### backend-delete
def backend_delete(request, pk):
     home = Home.objects.get( id=pk )
     home.delete()
     return redirect('homepage')

##### about
def about(request):
     page = 'create'
     abouts = About.objects.all()
     form = AboutForm()
     if request.method == 'POST':
          title = request.POST.get('title')
          form = AboutForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, "'{}', your create successfully!!!".format(title))
               return redirect('aboutpage')

     context ={
          'form':form,
          'abouts':abouts,
          'page':page
          }
     return render(request, 'layout/about.html',context)
             
##### edit -about
def about_edit(request, pk):
     page = 'edit'
     about = About.objects.get( id=pk )
     abouts = About.objects.all()
     form = AboutForm(instance=about)
     if request.method == 'POST':
          title = request.POST.get('title')
          form = AboutForm(request.POST, instance=about)
          if form.is_valid():
               form.save()
               messages.success(request, "'{}', your update successfully!!".format(title))
               return redirect('aboutpage')

     context = {
          'page':page,
          'about':about,
          'form':form,
          'abouts':abouts
     }
     return render(request, 'layout/about.html', context)

#### views 
def about_views(request, pk ):
     page = 'views'
     about = About.objects.get( id= pk )

     context = {
          'page':page,
          'about':about
     }     
     return render(request, 'layout/about-views.html', context)

#### about-delete
def about_delete(request, pk):
     about = About.objects.get( id=pk )
     email = request.POST.get('email')
     about.delete()
     messages.success(request, "your delete successfully!!")
     return redirect('aboutpage')

#### skill
def skill(request):
     page = 'create'
     skills = Skill.objects.all()
     form = SkillForm()
     if request.method == 'POST':
          title = request.POST.get('title')
          form = SkillForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, "you {} create successfully".format(title))
               return redirect('skillpage')

     context = {
          'page':page,
          'skills':skills,
          'form':form
     }
     return render(request, 'layout/skill.html', context)

### skill-edit
def sk_edit(request,pk):
     page = 'edit'
     skills = Skill.objects.all()
     skill = Skill.objects.get (id=pk)
     form = SkillForm(instance=skill)

     if request.method == 'POST':
          title = request.POST.get('title')
          form = SkillForm(request.POST, instance=skill)
          if form.is_valid():
               form.save()
               messages.success(request, " you {} update successfully".format(title))
               return redirect('skillpage')
     
     context = {
          'page':page,
          'skills':skills,
          'skill':skill,
          'form':form
          }
     return render(request, 'layout/skill.html', context)

#### skill-delete
def skl_del(request, pk):
     skill = Skill.objects.get(id=pk)
     skill.delete()
     return redirect('skillpage')

### category
def category(request):
     page = 'create'
     categories = Category.objects.all()
     form = CategoryForm()
     if request.method == 'POST':
          cate = request.POST.get('category')
          form = CategoryForm(request.POST)
          if form.is_valid():
               form.save()
               messages.success(request, "your {} create successfully!!".format(cate))
               return redirect('categorypage')

     context = {
          'form':form,
          'categories':categories,
     }
     return render(request, 'layout/category.html', context )

#### category-edit
def category_edit(request, pk):
     page = 'edit'
     category = Category.objects.get( id=pk )
     categories = Category.objects.all()
     form = CategoryForm(instance=category)

     if request.method == 'POST':
          cates = request.POST.get('category')
          form = CategoryForm(request.POST,instance=category)
          if form.is_valid():
               form.save()
               messages.success(request, "your {} update successfully".format(cates))
               return redirect('categorypage')

     context = {
          'page':page,
          'category':category,
          'categories':categories,
          'form':form,
     }
     return render(request, 'layout/category.html', context)

#### category-delete
def category_delete(request, pk):
     category = Category.objects.get( id=pk )
     category.delete()
     return redirect('categorypage')

#### image-page
def image(request):
     page = 'create'
     images = Iamge.objects.all()
     form = ImageForm()
     if request.method == "POST":
          title = request.POST.get('title')
          form = ImageForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, "you {} create successfully".format(title))
               return redirect('imagepage')

     context = {
          'images':images,
          'form':form,
          'page':page
     }
     return render(request, 'layout/image.html', context)

#### iamge-edit
def image_edit(request, pk):
     page = 'edit'
     images = Iamge.objects.all()
     image = Iamge.objects.get( id=pk )

     form = ImageForm(instance=image)
     if request.method == 'POST':
          title = request.POST.get('title')
          form = ImageForm(request.POST, request.FILES, instance=image)
          if form.is_valid():
               form.save()
               messages.success(request, "your {} update successfully".format(title))

     context ={
          'page':page,
          'form':form,
          'image':image,
          'images':images
     }
     return render(request, 'layout/image.html', context)

#### image-views
def image_views(request, pk):
     page = 'views'
     images = Iamge.objects.all()
     image = Iamge.objects.get( id=pk )

     context = {
          'page':page,
          'image':image,
          'images':images
     }
     return render(request, 'layout/image.html', context)

#### iamge-delete
def image_delete(request, pk):
     image = Iamge.objects.get(id=pk)
     image.delete()
     return redirect('imagepage')

### music
def music(request):
     musics = Music.objects.all()

     form = MusicForm()
     if request.method == 'POST':
          title = request.POST.get('title')
          form = MusicForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, "you {} create music successfully".format(title))
               return redirect('musicpage')

     context = {
          'form':form,
          'musics':musics
     } 
     return render(request, 'layout/mp-4.html', context)

def song(request):
     page = 'create'
     songs = Mp_3.objects.all()
     form = SongForm()
     if request.method == 'POST':
          title = request.POST.get('title')
          form = SongForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.success(request, "your {} create song successfully".format(title))
               return redirect("songpage")

     context = {
          'page':page,
          'form':form,
          'songs':songs
     }
     return render(request, 'layout/mp-3.html', context)

## song-edit
def songedit(request, pk):
     page = 'edit'
     songs = Mp_3.objects.all()
     song = Mp_3.objects.get( id=pk )
     form = SongForm(instance=song)

     if request.method == 'POST':
          title = request.POST.get('title')
          form = SongForm(request.POST, request.FILES, instance=song)
          if form.is_valid():
               form.save()
               messages.success(request, "your {} update song successfully".format(title))
               return redirect("songpage")

     context ={
          'form':form,
          'page':page,
          'songs':songs,
          'song':song
     }
     return render(request, 'layout/mp-3.html', context)

### song-del
def songdelete(request, pk):
     song = Mp_3.objects.get( id=pk )
     song.delete()
     return redirect('songpage')