Base views
    View
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

    TemplateView
        # TemplateView 继承自：
        from django.views.generic.base import TemplateResponseMixin # 模板渲染
        from django.views.generic.base import ContextMixin          # 上下文
        from django.views.generic.base import View                  # 视图
        1. 继承
        class HomeView(TemplateView):
            template_name = "home.html"
            # 可以重写方法
            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['self_define_var'] = "自定义上下文"
                return context

        2. 直接在url引用
        # url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),

    RedirectView
        # 其它请求所有重定向到首页
        # url(r'.*', RedirectView.as_view(url="http://www.baidu.com")),
        # query_string可以把query_string 带到重定向的url,默认False
        # [11/Jul/2018 04:20:39] "GET /app/inddsf/?a=100 HTTP/1.1" 302 0
        # [11/Jul/2018 04:20:39] "GET /app/index/?a=100 HTTP/1.1" 200 27
        url(r'.*', RedirectView.as_view(query_string=True, pattern_name="app:app_index")),



Generic display views

