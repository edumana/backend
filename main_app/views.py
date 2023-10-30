from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-published_date')
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # This will print the POST request body
        return super(BookViewSet, self).create(request, *args, **kwargs)
