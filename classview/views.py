from django.views.generic import TemplateView
from django.shortcuts import render

def permission_denied(request):
    return render(request, "403.html")


def page_not_found(request):
    return render(request, "404.html")


def page_error(request):
    return render(request, "500.html")


class HomeView(TemplateView):
    template_name = "home.html"
    # 可以重写方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['self_define_var'] = "自定义上下文"
        
        # 加入判断用户是否有用户管理逻辑
        has_group_add_perm = self.request.user.has_perm("auth.add_group")
        context['has_group_add_perm'] = has_group_add_perm
        return context
    
    
