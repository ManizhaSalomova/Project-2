# Create your models here.
from django import forms
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from rest_framework import status

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_id)


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Birth', null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def results_by_date(self):
            return self.date_of_birth + self.date_of_death
    
    def __str__(self):
            return str(self.name)


class Book(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='book')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.IntegerField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)    

    def __str__(self):
        return self.title
    
    def user_id(self):
        return self.user.user_id

    def name(self):
        return self.author.name
        


class UserBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='userBook')
    status = models.CharField(blank=True, null=True, max_length=10)
    rating = models.IntegerField(blank=False, null=False, help_text='1 - 5')
   

    def __str__(self):
        return self.rating

    def __str__(self):
        return self.status

    


