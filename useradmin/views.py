from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserListView(LoginRequiredMixin, ListView):
    queryset = User.objects.all().order_by("-date_joined")
    model = User
    template_name = "useradmin/user_list.html"
    context_object_name = 'users'
    paginate_by = 15
    