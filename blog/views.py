from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from .models import Post
from .forms import PostModelForm
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import  PermissionDenied

# 如果raise_exception = False 重定向都login
# 如果为true 会跳转到handler403
# 加上装饰函数即可控制是否能访问视图, permission粒度到model
@permission_required('blog.favor_post', raise_exception=True)
def post_show(request):
    # print(request.user)
    p = Post.objects.all().first()
    ps_dict = {}
    ps_dict.update({"title": f'{p.title}', "body": f'{p.body}'})
        
    return JsonResponse(ps_dict)




class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 3
    
    

class PostCreateView(CreateView):
    
    form_class = PostModelForm
    success_url = reverse_lazy("blog:post_list")
    template_name = "blog/post_create.html"
    
    
    @method_decorator(permission_required('blog.add_post', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        # 此处可以判断用户是否有权限进行
        # if not request.user.has_perm("blog.add_post"):
        #     raise PermissionDenied
        return  super().dispatch(request, *args, **kwargs)
        
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
    
    
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("blog:post_list")
    

# 测试object permission 装饰器
from guardian.decorators import permission_required_or_403

from django.http import HttpResponse
@permission_required_or_403("blog.delete_post", (Post, 'pk', 'pk'))
def post_detail(request, pk):
    p = Post.objects.get(pk=pk)
    return HttpResponse(p.title)
