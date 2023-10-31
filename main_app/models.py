from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(blank=False)
    edition = models.IntegerField(blank=True, default='1')
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    language = models.CharField(max_length=10, blank=True, default='')

    def __str__(self):
        return self.title