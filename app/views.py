import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from .models import Book, Author
from .forms import AuthorForm, BookCreateForm, BookUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone


# from utils.mixin import CommonMixin
# from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    # IndexView.as_view()--->view(request, *args, **kwargs)--->dispatch(request, *args, **kwargs)->get/post...(
    # request, *args, **kwargs)
    # 允许方法,小写
    # default:
    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    http_method_names = ["get"]
    # 可自定义类属性，通过as_view()传递进去
    test_attr = "testattr"
    def get(self, request, *args, **kwargs):
        return HttpResponse("app-index-01-with-{test_attr}".format(test_attr=self.test_attr))




# class HomeView(LoginRequiredMixin, CommonMixin, View):
#     template_name = 'home.html'
#     page_title = '概述'

# def get(self, request):
#     return render(request, self.template_name)

# TemplateView 继承自：
from django.views.generic.base import TemplateResponseMixin # 模板渲染
from django.views.generic.base import ContextMixin          # 上下文
from django.views.generic.base import View                  # 视图


class NewRedirectView(RedirectView):
    pattern_name = "app:app_index"
    query_string = True
    
    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class BookDetailView(DetailView):
    model = Book
    template_name = "app/book_detail.html"
    context_object_name = "book"
    
    # 默认使用pk_url_kwarg从queryset中进行过滤,
    # 如果期望自定义过滤字段时,需要同时定义以下两个属性
    # slug_url_kwarg = "name"
    # slug_field = "name"
    # 对应url_pattern: url(r'^detail/(?P<name>\w+)/$', BookDetailView.as_view(), name="app_detail"),
    
    # 下面是可以根据需求进行重写的方法
    # 此方法在 get_object()被重写时不会调用
    def get_queryset(self):
        # self.request
        filter_key = self.request.GET.get("f", 10)
        return super().get_queryset().filter(pk__in=[1,2])
        
    # 在此处决定返回的book对象
    # def get_object(self, queryset=None):
    #     queryset = super().get_object()
    #     return Book.objects.get(pk=3)

   
    # 追加上下文
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class BookListView(ListView):
    # get_queryset将不在执行
    queryset = Book.objects.all()
    model = Book
    template_name = "app/book_list.html"
    
    # 触发分页, 上下文中存在paginator对象, 和page_obj,is_paginated,等相关分页对象
    paginate_by = 3
    
    
    # def get_queryset(self):
    #     return super().get_queryset()
        
    # 当需要从url红获取字段值时，在get中
    def get(self, request, *args, **kwargs):
        author = kwargs.get('author',None)
        if author:
            # print(author)
            a_id = Author.objects.get(name=author).id
            # 这里能进行filter前提是,类属性在类定义时已经定义
            self.queryset = self.queryset.filter(author=a_id)
        return super().get(request, *args, **kwargs)
    
    
   
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"now": timezone.now()})
        # print(context)
        return context




class AuthorListView(ListView):
    # get_queryset将不在执行
    queryset = Author.objects.all()
    model = Author
    template_name = "app/author_list.html"
    
    # 触发分页, 上下文中存在paginator对象, 和page_obj,is_paginated,等相关分页对象
    paginate_by = 3



class AuthorWithFormView(FormView):
    '''
    get/post请求进来后触发相关的方法
    get--渲染template_name
    post--验证form有效性
    '''
    template_name = "app/author_formview.html"
    form_class = AuthorForm
    success_url = reverse_lazy("app:app_list")
    
    def form_valid(self, form):
        # 做一些其它处理
        return super().form_valid(form)


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']
    template_name = "app/author_create.html"
    #必须
    success_url = reverse_lazy("app:app_author_list")
    
    
# class TestMixin(object):
#     def form_valid(self, form):
#         self.object = form.save()
#         print(self.object)
#         return HttpResponse("ok")

class BookUpdateView(LoginRequiredMixin, UpdateView):
    # 继承自UpdateView时不可缺少
    model = Book
    # fields = ["price", "author"]
    # 使用BookCreateForm
    form_class = BookUpdateForm
    template_name = "app/book_update.html"
    success_url = reverse_lazy("app:app_book_list")


class TestMixin(object):
    '''处理ajax post请求
    返回json数据
    '''
    def form_valid(self, form):
        self.object = form.save()
        if self.object:
            print(self.object)
        else:
            print("save failed")
        return JsonResponse({"status":"0", "msg": "successfull create book", "redirect_url": self.success_url})
    
    def form_invalid(self, form):
        for label, err in form.errors.as_data().items():
            print(label, err[0].message)
            if len(err) > 0:
                err_str = '{}: {}'.format(label , err[0].message)
            return JsonResponse({'status': 1, 'msg': err_str})
        
    
class BookCreateView(LoginRequiredMixin, TestMixin, CreateView):
    # 使用form_class 或者model, fields
    # 通过集成ModelForm可以进行定制,表单控件
    # model = Book
    # fields = ['name', 'price', 'author']
    form_class = BookCreateForm
    template_name = "app/book_create.html"
    success_url = reverse_lazy("app:app_book_list")
    
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy("app:app_book_list")
    
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        book_name = self.object.name
        success_url = self.get_success_url()
        self.object.delete()
        return JsonResponse({"status":"0", "msg": "{}删除成功".format(book_name), "redirect_url": success_url})
        
    


    
