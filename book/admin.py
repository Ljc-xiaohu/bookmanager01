from django.contrib import admin
from book.models import BookInfo,PeopleInfo
# Register your models here.
#注册模型
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)