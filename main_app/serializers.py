from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField()  # This allows validate_author to temporarily pass validation

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'edition', 
                  'cover_image', 'language']

    def validate(self, data):
        author_name = data.get('author')
        author, _ = Author.objects.get_or_create(name=author_name)
        data['author'] = author
        
        return data

    def create(self, validated_data):
        author_name = validated_data.get('author')
        author, _ = Author.objects.get_or_create(name=author_name)
        validated_data['author'] = author
        return super(BookSerializer, self).create(validated_data)
