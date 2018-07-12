from django.conf.urls import url
from .views import *

app_name = "app"
urlpatterns = [
    url(r'^index/$', IndexView.as_view(test_attr="test_attr"), name="app_index"),
    
    url(r'^book/list/$', BookListView.as_view(), name="app_book_list"),
    url(r'^book/list/(?P<author>\w+)/$', BookListView.as_view(), name="app_list_by_author"),
    
    url(r'^author/list/$', AuthorListView.as_view(), name="app_author_list"),
    
    
    url(r'^detail/(?P<pk>\d+)/$', BookDetailView.as_view(), name="app_book_detail"),
    
    # url(r'^author/formview/$', AuthorWithFormView.as_view(), name="app_auth_with_form_view"),
    
    url(r'^author/create/$', AuthorCreateView.as_view(), name="app_author_create"),
    
    url(r'^book/create/$', BookCreateView.as_view(), name="app_book_create"),
    
    url(r'^book/update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name="app_book_update"),
    
    url(r'^book/delete/(?P<pk>\d+)/$', BookDeleteView.as_view(), name="app_book_delete"),
    
    
]
