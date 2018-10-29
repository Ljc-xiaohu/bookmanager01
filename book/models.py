from django.db import models
"""
    1.定义模型类
    2.生成迁移文件，执行迁移
        生成迁移文件   python manage.py makemigrations
        执行迁移（让数据库中有对应的表） python manage.py migrate
    3.操作增删改查
"""
# Create your models here.
class BookInfo(models.Model):


    #1.django的模型类需要继承自 models.Model
    #2.django自动会为我们创建一个id主键
    #书籍名
    name = models.CharField(max_length=10)


    def __str__(self):

        return self.name

class PeopleInfo(models.Model):

    #人物名
    name = models.CharField(max_length=10)
    #性别，布尔类型
    gender = models.BooleanField()
    #外键
    book = models.ForeignKey(BookInfo)


    def __str__(self):

        return self.name