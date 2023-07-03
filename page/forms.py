from fileinput import FileInput
from django import forms
from django.forms import EmailInput, TextInput, Textarea

from page.models import Contact, Products, OurServices


class CreateProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'description', 'image')

        labels = {
            'name':'Ürün İsmi',
            'description':'Ürün Açıklaması',
            'image':'Ürün Fotoğrafı'
        }

        widgets = {
            'name' : TextInput(attrs={"class":"form-control"}),
            'description': TextInput(attrs={"class":"form-control"}),
            'image': FileInput(),
        }

class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'subject', 'mail', 'message')

        labels = {
            'name':'Adınız ve Soyadınız',
            'subject':'Konu',
            'mail': 'E-mail Adresiniz',
            'message':'Mesajınız'
        }

        widgets = {
            'name' : TextInput(attrs={"class":"form-control"}),
            'subject': TextInput(attrs={"class":"form-control"}),
            'mail': EmailInput(attrs={'class':'form-control'}),
            'message':Textarea(attrs={"class":"form-control"}),
        }

class CreateOurServicesForm(forms.ModelForm):
    class Meta:
        model = OurServices
        fields = ('comment', 'file_upload')

        labels = {
            'comment':'Ürün Açıklaması',
            'file_upload':'Ürün Fotoğrafı'
        }

        widgets = {
            'comment' : TextInput(attrs={"class":"form-control"}),
            'file_upload': FileInput(),
        }

