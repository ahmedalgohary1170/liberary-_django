from django.shortcuts import render , redirect
from .models import Book
from . forms import BookForm

# Create your views here.

def book_list(request):
    data = Book.objects.all
    context = {'books':data}
    
    return render (request,'books/book_list.html',context)




def book_details(request,pk):
    data = Book.objects.get(id = pk)
    context = {'books':data}
    
    return render (request,'books/book_details.html',context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm()    
    return render(request,'books/new.html',{'form':form})



def edit_book(request,pk):
    book = Book.objects.get(id = pk)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm(instance=book)    
    return render(request,'books/edit.html',{'form':form})




def delete_book(request,pk):
    book = Book.objects.get(id = pk)
    book.delete()
    return redirect('/books/')