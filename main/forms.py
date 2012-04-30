# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", 
                  "password1", "password2")

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class TestForm(forms.Form):
    company = forms.CharField(label='Company Name', 
                              help_text='Enter company name (limit 30 characters)',
                              widget=forms.TextInput)
    subdomain = forms.CharField(label='Company Subdomain',
                                help_text="""Select a subdomain for your
                                account url e.g. subdomain.kolabria.com
                                (limit 30 characters, no spaces)""",
                                widget=forms.TextInput)
    username = forms.RegexField(label='Username', max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text = 'Required, 30 characters or less',
                                error_messages = {
                                    'invalid': 'Username can contain only'
                                    'letters, numbers and the following'
                                    'characters @.+-_'})
    email = forms.EmailField(label='Email', widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)


class CreateAccountForm(forms.Form):
    company = forms.CharField(label='Company Name', 
                              help_text='Enter company name (limit 30 characters)',
                              widget=forms.TextInput)
    subdomain = forms.CharField(label='Company Subdomain',
                                help_text="""Select a subdomain for your
                                account url e.g. subdomain.kolabria.com
                                (limit 30 characters, no spaces)""",
                                widget=forms.TextInput)
    username = forms.RegexField(label='Username', max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text = 'Required, 30 characters or less',
                                error_messages = {
                                    'invalid': 'Username can contain only'
                                    'letters, numbers and the following'
                                    'characters @.+-_'})
    email = forms.EmailField(label='Email', widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)


class ContactForm(forms.Form):    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'

    title = forms.CharField(label=u'title')
    email = forms.EmailField(label=u'email')
    web_site = forms.URLField(initial='http://', required=False)
    content = forms.CharField(label=u'content', widget=forms.Textarea)


CHOICES = (
           ('Web programlama', 'Web programlama'),
           ('GUI programlama', 'GUI programlama'),
           (u'Sistem yönetimi', u'Sistem yönetimi'),
           (u'Veritabanı sistemleri', u'Veritabanı sistemleri'),
           (u'İşletim sistemleri', u'İşletim sistemleri'),
)

class AuthorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'input-xlarge'


    focused_on = forms.MultipleChoiceField(
                                 label=u'Yöneliminiz',
                                 choices=CHOICES,
                                 help_text='Genel olarak hangi konular üzerinde yazabilirsiniz?'
                                 )
                
    projects = forms.CharField(
                               label=u'Projeler',
                               widget=forms.Textarea(),
                               required=False,
                               help_text='Lütfen adreslerini de yazınız.'
                               )
    
    extra_info = forms.CharField(
                                 label=u'Extra',
                                 widget=forms.Textarea(),
                                 required=False,
                                 help_text='Başka bildirmek istediğiniz şeyler'
                                 )
