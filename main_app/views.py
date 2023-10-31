from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-published_date')
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        return super(BookViewSet, self).create(request, *args, **kwargs)
    
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def create(self, request, *args, **kwargs):
        return super(AuthorViewSet, self).create(request, *args, **kwargs)
