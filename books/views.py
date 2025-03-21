from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm

def book_list(request):
    """View for displaying all books (accessible to both admin and students)"""
    if not request.user.is_authenticated:
        # If user is not logged in, don't show any books
        books = []
        messages.warning(request, 'Please login to view books.')
    else:
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def book_create(request):
    """View for creating a new book (authenticated users only)"""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Add New Book'})

@login_required
def book_update(request, pk):
    """View for updating an existing book (admin only)"""
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to update books.')
        return redirect('book_list')
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Update Book'})

@login_required
def book_delete(request, pk):
    """View for deleting a book (admin only)"""
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete books.')
        return redirect('book_list')
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
