from django.db import models
from django.urls import reverse
# Create your models here.


class List(models.Model):

    def get_absolute_url(self):
    	return reverse('view_list', args=[self.id])
    	#可以认为reverse的作用是传入一个django对应的url解析规则的名字和参数，返回对应的url硬编码，
    	#作用恰好和django解析硬编码的url时候相反
    	#redirect函数在获得一个模型对象作为参数时会自动调用get_absolute_url这个函数来获取url


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
