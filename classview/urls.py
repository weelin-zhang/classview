"""classview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from .views import HomeView, TemplateView

from app.views import NewRedirectView

from .views import permission_denied, page_error, page_not_found
handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    
    # url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),
    url(r'^home/$', HomeView.as_view(), name="home"),
    url(r'^app/', include('app.urls', namespace='app')),
    
    # 其它请求所有重定向到首页
    # url(r'.*', RedirectView.as_view(url="http://www.baidu.com")),
    # query_string可以把query_string 带到重定向的url,默认False
    # [11/Jul/2018 04:20:39] "GET /app/inddsf/?a=100 HTTP/1.1" 302 0
    # [11/Jul/2018 04:20:39] "GET /app/index/?a=100 HTTP/1.1" 200 27
    # url(r'.*', RedirectView.as_view(query_string=True, pattern_name="app:app_index")),
    url(r're/de/$', NewRedirectView.as_view()),
    
    # api
    url(r'^api/', include("api.urls", namespace="api")),
    
    # blog
    url(r'^blog/', include("blog.urls", namespace="blog")),
    
    # all in
    url(r'.*', RedirectView.as_view(pattern_name="home", query_string=True),),
]

