from django.urls import path

from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery-single/', views.gallery_single, name='gallery-single'),
    path('contact/', views.about, name='contact'),

]
