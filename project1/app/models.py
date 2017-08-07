from django.db import models
from django.db.models import CharField,DateField,ForeignKey,IntegerField
from django.contrib.auth.models import User
BALANCE_TYPE=((u'收入',u'收入'),(u'支出',u'支出'))
# Create your models here.
class Category(models.Model):#類別
    category=CharField(max_length=20)#20字
    user = models.ForeignKey(User, null=True)
    def __str__(self):#顯示的名稱
        return self.category

class Record(models.Model):#記帳記錄
    date=DateField()#日期
    description = CharField(max_length=300)#描述
    category = ForeignKey(Category,on_delete=models.SET_NULL,null=True)#類別
    #on_delete當Category被刪除,Record內的category也會被刪除  (models.CASCADE)
    #就表示不能被刪除(models.PROTECT)
    #關聯被刪除的時候,自動設定為NONE(models.SET_NULL())
    #跟上面依樣只是有預設值(models.SET_DEFAULT())
    #models.SET()
    cash=IntegerField()#金額
    balance_type=CharField(max_length=2,choices=BALANCE_TYPE)#收資類型
    user = models.ForeignKey(User, null=True)
    def __str__(self):#顯示的名稱
        return self.description
