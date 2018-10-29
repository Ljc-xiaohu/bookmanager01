from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.
from book.models import BookInfo

"""
1. 视图其实就是python的函数
2. 我们的视图函数的第一个参数必须是 请求对象
3. 我们的视图函数需要有一个 响应
"""

def index(request):

    # render 的第一个参数： request 请求
    # 第二参数是： 模板名字
    context = {
        'name':'阿三'
    }

    return render(request,'index.html',context=context)

    return HttpResponse('ok')



def booklist(request):

    #1. 调用模型来获取所有数据
    books = BookInfo.objects.all()
    # [BookInfo,BookInfo,]
    #2.将数据转换为 字典 to_dict
    #3.通过context(上下文) 传递给模板
    # django可以直接传递给模板 对象就可以
    context = {
        'books':books
    }
    return render(request,'booklist.html',context=context)

    return HttpResponse('booklist')


