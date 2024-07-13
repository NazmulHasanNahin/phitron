from django.shortcuts import render, get_object_or_404,redirect
from .models import Book, Category, Review
from .forms import ReviewForm



def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    category = request.GET.get('category')
    if category:
        books = books.filter(category__name=category)
    return render(request, 'book_app/book_list.html', {'books': books, 'categories': categories})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book_detail', book_id=book_id)
    else:
        review_form = ReviewForm()
    return render(request, 'book_app/book_detail.html', {'book': book, 'reviews': reviews, 'review_form': review_form})
