from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from stories.models import Contact, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'short_description',
            'description',
            'slug',
            'image',
            'owner',
            'category',
            'tags'
        )

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short description'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Slug'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Image'
            }),
            'owner': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'select owner'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'select owner'
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'select owner'
            }),

        }


class ContactForm(forms.ModelForm):
    # name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Your name'
    # }))
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message'
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            })
        }

#    def clean_email(self):
#        email_data = self.cleaned_data['email']
#        if not email_data.endswith('@gmail.com'):
#            raise forms.ValidationError('Email must be gmail')
#        return email_data

    # def clean(self):
    #     email = self.cleaned_data['email']
    #     if not email.endswith('@gmail.com'):
    #         raise forms.ValidationError('Email must be gmail')
    #     return super().clean()



#class ContactForm(forms.Form):
#    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={
#        'class': 'form-control',
#        'placeholder': 'Your name'
#    }))
#    email = forms.EmailField(label='Email', max_length=40)
#    subject = forms.CharField(label='Subject', max_length=255)
#    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
#        'class': 'form-control'
#    }))
