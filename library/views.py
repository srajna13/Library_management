from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Records

# Create your views here.

def index(request):
    return render(request,'library/base.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

@login_required
def my_borrows(request):
    records = Records.objects.filter(user=request.user)
    return render(request, 'library/my_borrows.html', {'records': records})


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.is_available:
        Records.objects.create(user=request.user, book=book)
        book.is_available = False
        book.save()

    return redirect('book_list')

@login_required
def return_book(request,record_id):
    record=get_object_or_404(Records,id=record_id)
    print(record)

    if not record.returned:
        record.returned = True
        record.return_date = timezone.now()
        record.book.is_available = True
        record.book.save()
        record.save()

    return redirect('my_borrows')