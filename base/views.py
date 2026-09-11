from django.shortcuts import render, redirect, get_object_or_404
from .models import Article,Genre
from .forms import ArticleForm,GenreForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def create_genre(request):
    if request.method =='POST':
        form = GenreForm(request.POST or None)
        if form.is_valid():  # it checks if the form variables has data or not
            form.save()  #creation operation completes
            messages.success(request,'Genre added Succesfully!...')
            return redirect('read_genre')
    else:
        form = GenreForm()
    return render(request,'create_genre.html', {'form':form}) 

def read_genre(request):
    search =request.GET.get('q')
    data = Genre.objects.all()
    if search:
        data = Genre.objects.filter(
            Q(name__icontains = search)|
            Q(desc__icontains = search)|
            Q(rating__icontains = search)
        )
    else:
        data =Genre.objects.all()
    return render(request,'read_genre.html' , {'data':data, 'search':search})
    

def update_genre(request,pk): 
    data = get_object_or_404(Genre, id = pk)
    if request.method =='POST':
        form = GenreForm(request.POST or None, instance=data) # instance = data it is responsible for updating the data
        if form.is_valid():  # it checks if the form variables has data or not
            form.save()  #creation operation completes
            messages.success(request,'Genre updated Succesfully!...')
            return redirect('read_genre')
    else:
        form = GenreForm(instance=data)
    return render(request,'update_genre.html', {'form':form})

def delete_genre(request,pk):
    data = get_object_or_404(Genre, id = pk)
    if request.method =='POST':
        data.delete()
        messages.success(request, 'Genre deleted successfully!...')
        return redirect('read_genre')
    return render(request,'delete_genre.html',{'data':data})



#ARTICLE

@login_required(login_url='signin')
def home(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article created successfully')
            return redirect('read_article')
    else:
        form = ArticleForm()

    return render(request, 'home.html', {'form': form})

#READ
@login_required(login_url='signin')
def read_article(request):
    search = request.GET.get('q')
    if search:
        data = Article.objects.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(author_name__icontains=search) |
            Q(tags__icontains=search)|
            Q(created_at__icontains=search)
        )
    else:
        data = Article.objects.filter(is_deleted = False)

    return render(request, 'read_article.html', {'data':data, 'search':search})

#UPDATE
@login_required(login_url='signin')
def update_article(request, pk):   # view
    data = get_object_or_404(Article, id=pk, is_deleted = False)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=data)

        if form.is_valid():   # it checks if the form variable has data or not
            form.save()       # creation operation completes
            messages.success(request, 'Article updated successfully!...')
            return redirect('read_article')

    else:
        form = ArticleForm(instance=data)

    return render(request, 'update_article.html', {'form': form})

#DELETE
@login_required(login_url='signin')
def delete_article(request, pk):
   data = get_object_or_404 (Article, id=pk, is_deleted = False)
   if request.method == "POST":
       # data.delete()  ----> it will permanently delete the record
       data.is_deleted = True # deleting data partially 
       data.deleted_at = timezone.now()
       data.save() 
       messages.success(request, 'Article deleted successfully!...')
       return redirect('read_article')
   return render(request, 'delete_article.html',{'data':data})

#HISTORY
@login_required(login_url='signin')
def history_article(request):
    search = request.GET.get('q')
    if search:
        data = Article.objects.filter(
            Q(title__icontains=search) |
            Q(summary__icontains=search) |
            Q(author_name__icontains=search) |
            Q(tags__icontains=search)|
            Q(deleted_at__icontains=search)
        )
    else:
        data = Article.objects.filter(is_deleted = True)

    return render(request, 'history_article.html', {'data':data, 'search':search})

#RESTORE
@login_required(login_url='signin')
def restore_article(request, pk):
    data = get_object_or_404(Article, id=pk, is_deleted=True)
    if request.method == "POST":
           data.is_deleted = False 
           data.deleted_at = None
           data.save() 
           messages.success(request, 'Article Restored successfully!...')
           return redirect('history_article')
    return render(request, 'restore_article.html',{'data':data})