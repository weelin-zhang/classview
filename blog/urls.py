from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^posts/$', post_show, name="post_show"),
    url(r'^create/$', PostCreateView.as_view(), name="post_create"),
    url(r'^list', PostListView.as_view(), name="post_list"),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name="post_update"),
]
