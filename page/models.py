from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    message = models.TextField()
    subject = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'İletişim formu Ayarları'
        verbose_name_plural = 'İletişim Formları'

    def __str__(self):
        return f"{self.name}"  
    
class OurServices(models.Model):
        name = models.CharField(max_length=100, null=True)
        comment = models.TextField(null=True) 
        file_upload = models.ImageField(upload_to='product_images/', null=True)
        class Meta:
            verbose_name = 'Hizmetlerimiz Bölümü Ayarları'
            verbose_name_plural = 'Hizmetlerimiz Bölümü Formu'

        def __str__(self):
            return f"{self.name}"

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    class Meta:
        verbose_name = 'Ürünlerimiz Bölümü Ayarları'
        verbose_name_plural = 'Ürünlerimiz Bölümü Formu'

    def __str__(self):
        return self.name
