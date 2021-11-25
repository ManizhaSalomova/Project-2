from rest_framework import serializers
from .models import User
from .models import Author
from .models import Book
from .models import UserBook


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('pk', 'user_name', 'user_id', 'email', 'created_date')


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('pk','user', 'user_id', 'author', 'name','title', 'description','isbn', 'year')


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('pk','name', 'date_of_birth', 'date_of_death')


class UserBookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserBook
        fields = ('pk', 'book', 'status', 'rating')
        












