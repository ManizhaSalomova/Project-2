"""book_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),

    path('', views.user_list),
    url(r'^api/users/$', views.user_list),
    url(r'^api/users/(?P<pk>[0-9]+)$', views.getUser),

    path('authors/', views.author_list),
    url(r'^api/authors/$', views.author_list),
    url(r'^api/authors/(?P<pk>[0-9]+)$', views.getAuthor),

    path('books/', views.book_list),
    url(r'^api/books/$', views.book_list),
    url(r'^api/books/(?P<pk>[0-9]+)$', views.getBook),

    path('userbooks/', views.userbook_list),
    url(r'^api/userbooks/$', views.userbook_list),
    url(r'^api/userbooks/(?P<pk>[0-9]+)$', views.getUserBook)

]
