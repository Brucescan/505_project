from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name="店铺名称")
    phone = models.CharField(max_length=50, verbose_name="联系电话")
    address = models.CharField(max_length=200, verbose_name="地址")
    tags = models.CharField(max_length=100, verbose_name="标签")  # 假设标签是一个字符串
    rating = models.FloatField(default=0.0, verbose_name="评分")

    def __str__(self):
        return self.name
