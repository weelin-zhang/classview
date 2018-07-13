from django.conf.urls import url, include
# from .views import (AuthorListView, AuthorDetailView, CreateBookView)
from .views import *
from . import views
from rest_framework.authtoken import views as rf_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', views.AuthorViewSet)
router.register('book', views.BookViewSet)


urlpatterns = [
   
    # rest_framework自带的获取用户token的视图,post,username&password with json format
    url(r'^v1/authtoken/$', rf_views.obtain_auth_token, name='api_auth_token'),
    
    
    # authors
    url(r'^v1/author/$', AuthorListView.as_view(), name='author_list'),
    url(r'^v1/author/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),
    url(r'^v1/author/create/', CreateAuthorView.as_view(), name="create_author"),
    url(r'^v1/author/operate/(?P<pk>\d+)/$', UpdateDeleteAuthorView.as_view(), name="operate_author"),
    
    # books
    url(r'^v1/book/$', BookListView.as_view(), name='book_list'),
    url(r'^v1/book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'^v1/book/create/', CreateBookView.as_view(), name="create_book"),
    url(r'^v1/book/operate/(?P<pk>\d+)/$', UpdateDeleteBookView.as_view(), name="operate_book"),
    
    
    # viewset
    url(r'^v2/', include(router.urls)),

]