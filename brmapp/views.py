from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Book

# Create your views here.
def home(request):
    books=Book.objects.all()
    return render(request,'starter.html',{
        'books':books
    })
    #return render(request,)
def viewbook(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_books = paginator.get_page(page_number)
    return render(request, 'home.html',{
        'books':books,
        'page_books':page_books
    })

def add_book(request):
    if request.method == 'POST':
        title = request.POST['book_title']
        picture=request.FILES['book_image']
        author = request.POST['book_author']
        price = request.POST['book_price']
        rating=request.POST['book_rating']
        description=request.POST['book_description']
        #create model object
        book = Book(title=title,picture=picture,author=author,price=price,rating=rating,description=description)
        book.save() #save book object
        book_id=book.id
        return redirect(f'/show-book/{book_id}')
    return render(request,'add-book.html') 

def delete_book(request,book_id):
    book=Book.objects.get(pk=book_id)
    book.delete()
    return redirect('/')

def edit_book(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'edit-book.html',{
        'book':book
    })
def do_edit_book(request,book_id):
    book=Book.objects.get(id=book_id)
    book.title=request.POST['book_title']
    book.author=request.POST['book_author']
    book.price=request.POST['book_price']
    book.description=request.POST['book_description']
    book.rating=request.POST['book_rating']
    book.save()
    return redirect(f'/show-book/{book_id}')

def show_book(request,book_id):
    book=Book.objects.get(pk=book_id)
    return render(request,'show-book.html',{'book':book})