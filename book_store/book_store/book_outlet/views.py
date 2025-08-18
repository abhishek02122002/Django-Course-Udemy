from django.shortcuts import render,get_object_or_404
from .models import Book
from django.db.models import Avg,Min,Max
# Create your views here.
def index(request):
     books = Book.objects.all().order_by("title")
     # iss order wale me aagr - ka sign laag de to wo apne aap hi negative way me ho jata hai. 
     total_books = books.count()
     avg_rating = books.aggregate(Avg("rating"))
     return  render(request,"book_outlet/index.html",{
          "books":books,
          "total_books":total_books,
          "avg_rating":avg_rating
     })

def book_details(request,slug):
     # book = Book.objects.get(pk=id)
     book = get_object_or_404(Book,slug=slug)
     return render(request,"book_outlet/book_details.html",{
          "title":book.title,
          "author":book.author,
          "rating":book.rating
     })
     