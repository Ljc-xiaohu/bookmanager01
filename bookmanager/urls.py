"""bookmanager URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin

#2. urlpatterns 是固定写法，我们的url就是采用这样的变量名

urlpatterns = [

    #3. 列表中的元素就是 url 元素
    #4. 参数1： 正则
    #   r 不用我们字符串中的/ 转义
    #   ^ 以什么开头     $以什么结尾

    #5.用户在url中输入的url，会顺次的和 urlpatterns中的元素顺次进行匹配，如果有匹配合适的结果
    # 则引导到对应的视图中
    #如果没有匹配合适的结果 则返回 404

    #6. http://127.0.0.1:8000/admin/book/bookinfo/?a=100
    # url正则匹配的规则： url中的 http://ip:port/  和 get post参数不进行正则匹配
    #admin/book/bookinfo/
    #http://127.0.0.1:8000/index/
    # index/
    #http://127.0.0.1:8000/book/index/
    #book/index/
    #book/booklist/

    url(r'^admin/', admin.site.urls),

    # 引导规则： 所有以 admin/ 开始的 都引导了 admin站点中
    # 所有不是以 admin/ 开始的 都引导到 book 子应用中

    #2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

    # url(r'^',include('book.urls')),
    #url(r'^book/$',include('book.urls')),  错误的
    url(r'^book/',include('book.urls')),
]
