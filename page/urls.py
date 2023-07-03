from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('anasayfa', views.index,  name="page_index"),
    path('iletisim', views.ContactFormView.as_view(),  name="page_contact"),
    path('hizmetlerimiz', views.services,  name="page_services"),
    path('urunlerimiz', views.products,  name="page_products"),
]