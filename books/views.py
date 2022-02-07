
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
import json
from django.views.generic import ListView , DetailView
from books.models import Book,Review
from django.contrib.auth.mixins import LoginRequiredMixin
from books.form import ReviewForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

class BookListView(ListView):
    #template_name = 'books/index.html'
    #context_object_name = 'books'
    def get_queryset(self):
        return Book.objects.all()

'''def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html',context)'''



class BookDetailView(DetailView):
    model = Book


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['authors'] = context['book'].author.all()
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['form'] = ReviewForm()

        return context



'''def show(request, id):
    try:
        singleBook = Book.objects.filter(id=id).first()
    except Book.DoesNotExist:
        raise Http404("Ops...!!!  Book Not Found")
    review = Review.objects.filter(book_id=id).order_by('-created_at')
    context = {'book':singleBook , 'reviews':review}
    return render(request, 'books/show.html',context)  '''

def review(request, id):
    if request.user.is_authenticated:
        body = request.POST['body']
        newReview = Review(body=body, book_id=id, user=request.user)

        
        if len(request.FILES) != 0:
            image = request.FILES['image']
            fs= FileSystemStorage()
            name = fs.save(image.name, image)
            newReview.image = fs.url(name)
        newReview.save()
    return redirect('/')


def author(request , author):
    books = Book.objects.filter(author__name = author)
    context = {'book_list': books }
    return render(request , 'books/book_list.html' , context)






