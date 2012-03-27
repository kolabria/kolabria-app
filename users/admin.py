# -*- coding: utf-8 -*-

from django.contrib import admin
from pythontr_org.users.models import Profile

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from pythontr_org.users.mails import decline_author_requests_mail, accept_author_requests_mail


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['web_site', 'about', 'city']    
    list_display  = ('user', 'web_site', 'city')


class CoolUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    actions      = [
                    'accept_author_requests',
                    'decline_author_requests',
                    'make_author',
                    'make_standart_user'
                    ]
    
    authors_group        = Group.objects.get(name='Yazarlar')
    standart_users_group = Group.objects.get(name='Sıradan üyeler')
    
    
    def accept_author_requests(self, request, queryset):
        for user in queryset:
            if not user in self.authors_group.user_set.all():
                user.groups.clear()
                user.groups.add(self.authors_group)             
                
                accept_author_requests_mail(user)                
        self.message_user(request, u'Seçili kullanıcıların yazarlık başvuruları onaylandı.')

    accept_author_requests.short_description = u'Seçili kullanıcıların yazarlık başvurusunu onayla'
    
    
    def decline_author_requests(self, request, queryset):
        for user in queryset:
            user.groups.clear()
            
            decline_author_requests_mail(user)
            
        self.message_user(request, u'Seçili kullanıcıların yazarlık başvuruları reddedildi.')
        
    decline_author_requests.short_description = u'Seçili kullanıcıların yazarlık başvurusunu reddet'
    
    
    def make_author(self, request, queryset):
        for user in queryset:
            user.groups.clear()
            user.groups.add(self.authors_group)
            
        self.message_user(request, u'Seçili kullanıcılar yazar yapıldı.')
    make_author.short_description = u'Seçili kullanıcıları yazar yap (E-posta göndermez.)'
    
    
    def make_standart_user(self, request, queryset):
        for user in queryset:
            user.groups.clear()
            user.groups.add(self.standart_users_group)
        
        self.message_user(request, u'Seçili kullanıcılar sıradan üye yapıldı.')
    make_standart_user.short_description = u'Seçili kullanıcıları standart üye yap (E-posta göndermez.)'
    

admin.site.register(Profile, ProfileAdmin)

admin.site.unregister(User)
admin.site.register(User, CoolUserAdmin)