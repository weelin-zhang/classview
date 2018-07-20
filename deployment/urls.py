from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list/', DeploymentListView.as_view(), name="deployment_list"),
    url(r'^perm/', ProjectDeployManage.as_view(), name="deployment_perm"),
    url(r'^checkperm/', CheckPermView.as_view(), name="deployment_checkperm"),
]
