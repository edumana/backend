from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True, required=False)  # Optional during updates
    author = AuthorSerializer(read_only=True)  # Nested AuthorSerializer for read operations

    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'published_date', 'edition', 'cover_image', 'language', 'author']
        read_only_fields = ['author']

    def create(self, validated_data):
        author_name = validated_data.pop('author_name', None)  # Pop using author_name, handle case where it might be missing
        if author_name:
            author, created = Author.objects.get_or_create(name=author_name)
            validated_data['author'] = author
        return super().create(validated_data)

