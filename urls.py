from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    #path('life/', views.life, name='life'),
    path('health/', views.health, name='health'),
    #path('rssa/', views.rssa, name='rssa'),
    #path('notary/', views.notary, name='notary'),
    #path('aboutUs/', views.aboutUs, name='aboutUs'),
    #path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('privacy/', views.privacy, name='privacy'),
]