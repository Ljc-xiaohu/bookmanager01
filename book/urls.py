#coding:utf8
# 既然都是urls 书写形式和 bookmanager.urls是一样的
from django.conf.urls import url
from book.views import index,booklist

urlpatterns = [
    # 参数1： 正则
    # 参数2： 视图函数名
    # book/index/

    #url(r'^book/index/$',index),    #1
    url(r'^index/$',index),         #2


    # booklist/
    url(r'^booklist/$',booklist),
]