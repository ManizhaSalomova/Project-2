from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Book, Author, UserBook

# Register your models here.

class UserList(admin.ModelAdmin):
    list_display = ('user_id','user_name', 'email', 'created_date')
    list_filter = ('user_id','user_name', 'email', 'created_date')
    search_fields = ('user_id','user_name', 'email')
    ordering = ('user_id',)


class AuthorList(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'date_of_death')
    list_filter = ('name', 'date_of_birth')
    search_fields = ('name', 'date_of_death')
    ordering = ['name']   



class BookList(admin.ModelAdmin):
    list_display = ('user', 'author','title', 'description','isbn', 'year')
    list_filter = ('user', 'author', 'title', 'description')
    search_fields = ('user', 'author', 'title')
    ordering = ['user', 'author']



class UserBookList(admin.ModelAdmin):
    list_display = ('book','rating', 'status')
    list_filter = ('book','rating', 'status')
    search_fields = ('book','rating')
    ordering = ['book']



admin.site.register(User, UserList)
admin.site.register(Author, AuthorList)
admin.site.register(Book, BookList)
admin.site.register(UserBook, UserBookList)
