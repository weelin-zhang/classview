from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

def permission_denied(request):
    return render(request, "403.html")


def page_not_found(request):
    return render(request, "404.html")


def page_error(request):
    return render(request, "500.html")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    
    # 可以重写方法
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['self_define_var'] = "自定义上下文"
        return context
    
# 测试几个响应
# from django.views.generic.base import View
# from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
# from django.http import HttpResponseForbidden, HttpResponseNotFound
# class HomeView(View):
#     def get(self, request):
        # raise PermissionDenied
        # return HttpResponseForbidden()
