from django.conf.urls import url, include
from .views import *
from . import views
from rest_framework.authtoken import views as rf_views
from rest_framework import routers

from  rest_framework.schemas import  get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from .views import CustomAuthToken

router = routers.DefaultRouter()
router.register('author', views.AuthorViewSet)
router.register('book', views.BookViewSet)
router.register('blog', views.BlogViewSet)

# router_blog = routers.DefaultRouter()
# router_blog.register('blog', views.BlogViewSet)


schema_view = get_schema_view(title='Books&Authors API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
   
    # rest_framework自带的获取用户token的视图,post,username&password with json format
    url(r'^authtoken/$', CustomAuthToken.as_view(), name='api_auth_token'),
    # url(r'^authtoken/$', rf_views.obtain_auth_token, name='api_auth_token'),
    
    
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
    # url(r'^v2_blog/', include(router_blog.urls)),
    
    
    # swagger
    url(r'^docs/', schema_view, name="docs"),
]