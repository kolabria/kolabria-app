# -*- coding: utf-8 -*-

"""
    'posts' uygulaması için functional ve unit testleri
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from pythontr_org.posts.models import Post, Category



class PostFunctionals(TestCase):
    """
    
        'Post' modeli ile ilgili functional test.    
        
    """
    
    def setUp(self):        
        self.client.login(username='yigit', password='1234')
        
    
    def test_get_index(self):
        """
        
            Index sayfasına istek gönderir.
            200 durum kodu döndürmelidir.
            
        """
        
        response = self.client.get(reverse('posts:index'))
        
        self.assertEqual(response.status_code, 200)        
        self.assertIsNotNone(response.context['object_list']) # generic view
        
        
    def test_get_show(self):
        """
        
            Show sayfasına istek gönderir.
            200 durum kodu döndürmelidir.
            
        """
        
        posts = Post.objects.filter(published = True)
        
        for post in posts:
            response = self.client.get(post.get_absolute_url())
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['post'].title, post.title)
            
            self.assertEqual(post.read_count + 1, response.context['post'].read_count)
            
            
    def test_get_show_should_return_404(self):
        """
        
            Show sayfasına istek gönderir.
            Yanlış bir id ile istek yapılır.
            404 hata kodu döndürmelidir.
            
        """
        
        BAD_IDS = ['wrong-slug-one', 'wrong-and-bad-slug']
        
        for bad in BAD_IDS:
            response = self.client.get(reverse('posts:show', args=['django', bad]))
            
            self.assertEqual(response.status_code, 404)
            
            
    def test_should_search(self):
        """
        
            Search sayfasına istek gönderir.
            django ve tkinter için arama yapar.
            
        """
                
        SEARCH_LIST = ('django', 'tkinter')
        
        for q in SEARCH_LIST:
            response = self.client.get(reverse('posts:search'), {'q': q})
            
            self.assertIsNotNone(response.context['posts'])
    
    
    def test_get_my_posts(self):
        """
            
            Gönderilerim sayfasına erişmelidir.
            
        """

        response = self.client.get(reverse('posts:my_posts'))        
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['posts'])

            

        
class CategoryFunctionals(TestCase):
    """
    
        'Category' modeli ile ilgili functional test.
        
    """
        
    
    def test_should_get_show_category(self):
        """
        
            Her kategorideye bağlı gönderileri listeleme
            testi.
            
        """
        
        categories = Category.objects.all()
        
        for cat in categories:
            response = self.client.get(cat.get_absolute_url())
            
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.context['posts'])
        
            self.assertEqual(len(cat.post_set.all()), len(response.context['posts']))
            
            
    def test_should_raise_404_with_bad_id(self):
        """
        
            Yanlış id verilirse 404 döndürmelidir.
            
        """
        
        response = self.client.get(reverse('posts:show_category', args=['hatali']))
        
        self.assertEqual(response.status_code, 404)
         