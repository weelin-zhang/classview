from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Deployment
# Create your views here.

from guardian.shortcuts import get_objects_for_user



class DeploymentListView(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Deployment
    context_object_name = "deployments"
    template_name = "deployment/deployment_list.html"
    
    
    def get_queryset(self):
        user = self.request.user
        perms = ['deployment.view_deployment']
        queryobject = get_objects_for_user(user, perms, use_groups=False,
                                                                                        accept_global_perms=False)
        return queryobject
        # return super().get_queryset()
        
    
    
