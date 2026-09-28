from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index_view,name='index_page'),
         path('about/',about_view,name='about_page'),
         path('login/',login_view, name='login_page'),
         path('register/',register_view,name='Register_page'),
]



