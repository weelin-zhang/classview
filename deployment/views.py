from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from deployment.models import Project
from .models import Deployment

from guardian.shortcuts import get_perms, assign_perm, remove_perm
# Create your views here.

from guardian.shortcuts import get_objects_for_user



class DeploymentListView(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Deployment
    context_object_name = "deployments"
    template_name = "deployment/deployment_list.html"
    
    
    def get_queryset(self):
        user = self.request.user
        perms = ['deployment.deploy_project']
        project_queryobject = get_objects_for_user(user, perms, use_groups=False, accept_global_perms=False)
        deploymentqueryset = []
        for p in project_queryobject:
            deploymentqueryset.extend(p.deployments.all())
        return deploymentqueryset
        # return super().get_queryset()
        
        
class ProjectDeployManage(LoginRequiredMixin, View):
    perm = 'deploy_project'
    
    def get(self, request):
        ret = {}
        if request.user.is_superuser:
            print("超级管理员")
            # 超级用户可以为一级业务线负责人,二级业务负责人和普通开发人员设置权限
            # users = [ u for u in User.objects.all() if not u.is_superuser]
            
            # 超级用户只可以为一级业务线负责人设置权限
            users = [ u for u in User.objects.all() if len(u.toplines.all()) >=1 ]
        elif request.user.toplines.all():
            print("顶级负责人")
            # 一级负责人可以为二级负责人和普通开发人员设置权限
            # users = [ u for u in User.objects.all() if len(u.toplines.all()) == 0 and not u.is_superuser]
            
            # 一级负责人可以为二级负责人人员设置权限
            users = [ u for u in User.objects.all() if len(u.businesslines.all()) >=1 ]
        else:
            print("二级负责人")
            # 二级负责人只能给普通开发人员设置权限
            users = [ u for u in User.objects.all() if len(u.toplines.all()) == 0 and len(u.businesslines.all()) == 0
                                                                                  and not u.is_superuser]
            
        projects = [ p for p in Project.objects.all() if self.perm in get_perms(request.user, p)]
        ret['users'] = users
        ret['projects'] = projects
        return render(request, "deployment/deployment_perm.html", context=ret)
    
    def post(self, request):
        code, msg = "1",""
        u_id = request.POST.get("selectuser")
        u_obj = User.objects.filter(pk=int(u_id))
        p_id = request.POST.get("selectproject")
        p_obj = Project.objects.filter(pk=int(p_id))
        
        if not p_obj or not u_obj:
            msg = "不存在该项目"
            
        try:
            print(u_obj, p_obj)
            assign_perm(self.perm, u_obj[0], p_obj[0])
            code = "0"
            msg="权限关联成功"
        except Exception as e:
            msg = str(e)
            print(e)
        
        return JsonResponse({"status": code, "msg": msg})
    
    def delete(self, request):
        import json
        code, msg = "1",""
        args_str = request.body.decode("UTF-8")
        arg_dict = dict(arg.split("=") for arg in args_str.split("&") if "csrfmiddlewaretoken" not in arg)
        
        u_id = arg_dict.get("selectuser", 0)
        u_obj = User.objects.filter(pk=int(u_id))
        p_id = arg_dict.get("selectproject", 0)
        p_obj = Project.objects.filter(pk=int(p_id))
    
        if not p_obj or not u_obj:
            msg = "不存在该项目"
    
        try:
            remove_perm(self.perm, u_obj[0], p_obj[0])
            code = "0"
            msg="权限解除成功"
        except Exception as e:
            msg = str(e)
            print(e)
        
        return  JsonResponse({"msg": msg, "status": code})
