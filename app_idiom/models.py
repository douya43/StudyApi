from django.db import models
from datetime import datetime


# 会员数据模型
class Member(models.Model):
    id = models.AutoField # 编号
    openid = models.CharField(max_length=88)     # 微信用户id
    nickname = models.CharField(max_length=100)  # 用户名
    avatar = models.CharField(max_length=255)  # 头像
    sesion = models.IntegerField(max_length=11, default=0)       # 通过关卡
    addtime = models.DateTimeField(default=datetime.now(),)  # 注册时间

    def __repr__(self):
        return '<User %r>' % self.nickname
    class Meta:
        db_table = 'member'  # 数据库表名

# 考题数据模型
class Exam(models.Model):
    id = models.AutoField  # 编号
    pictureUrl = models.CharField(max_length=255) # 图片url
    answer = models.CharField(max_length=20) # 答案
    candidates = models.CharField(max_length=100)# 备选项
    addtime = models.DateTimeField(default=datetime.now(),)   # 添加时间
    def __repr__(self):
        return '<Exam %r>' % self.answer

    class Meta:
       db_table = 'exam'  # 数据库表名
