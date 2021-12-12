from django.test import SimpleTestCase
from django.urls import reverse, resolve
from book.views import user_list, getUser, author_list, getAuthor, book_list, getBook, userbook_list, getUserBook


class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolves(self):
        url = reverse('list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_list)

    def test_author_url_is_resolves(self):
        url = reverse('author')
        print(resolve(url))
        self.assertEquals(resolve(url).func, author_list)


    def test_book_url_is_resolves(self):
        url = reverse('book')
        print(resolve(url))
        self.assertEquals(resolve(url).func, book_list)
    
    def test_userbook_url_is_resolves(self):
        url = reverse('userbook')
        print(resolve(url))
        self.assertEquals(resolve(url).func, userbook_list)