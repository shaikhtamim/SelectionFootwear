from django.urls import path

from gallery import views as gallery_views
from products import views as product_views
from website import views
from inquiry import views as inquiry_views

urlpatterns = [
    path('', views.home, name='home'),
    path('women/', product_views.women, name='women'),
    path('kids/', product_views.kids, name='kids'),
    path('gallery/', gallery_views.gallery, name='gallery'),
    path('contact/', inquiry_views.contact, name='contact'),
    path('about/', views.about, name='about'),
]