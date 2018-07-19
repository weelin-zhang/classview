from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'list/', UserListView.as_view(), name="user_list"),
]
