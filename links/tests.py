# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


from pythontr_org.links.models import Link



class LinksFunctionals(TestCase):
    
    fixtures = ['links.json', 'auth.json']
    
    
    def setUp(self):
        self.client.login(username='yigit', password='1234')
        
        self.link_informations = {
                                  'title': 'Django Project',
                                  'href': 'https://www.djangoproject.com/',
        }
        
        self.CONFIRMED_TEXT = u'Teşekkürler. Bağlantı başarı ile eklendi. Yöneticiler onayladığında listede yerini alacaktır.'
    
    
    def test_index_page(self):
        """
            Bağlantılar anasayfasını test eder.
        """

        response = self.client.get(reverse('links:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['links'])
        
        self.assertEqual(len(Link.objects.all()), len(response.context['links']))
    
    
    def test_get_new_link_page(self):
        """
            Yeni bağlantı ekleme sayfasına GET isteği yap.
        """
        
        response = self.client.get(reverse('links:new'))
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])
      
        
    def test_post_new_link_page(self):
        """
            Yeni bağlantı ekleme sayfasına POST isteği yapar.
        """
        
        count = Link.objects.count()
        
        response = self.client.post(reverse('links:new'), self.link_informations, follow=True)
        
        self.assertRedirects(response, reverse('users:settings'))
        self.assertContains(response, self.CONFIRMED_TEXT)
        
        self.assertNotEqual(count, Link.objects.count())
        self.assertEqual(Link.objects.latest().title, self.link_informations['title'])
        
        self.assertFalse(Link.objects.latest().confirmed)
        


class LinkUnits(TestCase):
    """
        Bağlantı modelinin unit testleri.
    """
    
    fixtures = ['auth.json', 'links.json']
    
    
    def setUp(self):
        self.link_informations = {
                                  'title': 'Django Project',
                                  'href': 'https://www.djangoproject.com/',
        }
    
    
    def test_create_new_link(self):
        """
            Yeni bağlantı yaratma test.
        """
        
        link = Link.objects.create(**self.link_informations)
        
        self.assertTrue(link)
        
        
    
        