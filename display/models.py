from django.db import models


# Create your models here.
class Quote(models.Model):
    # 文本
    text = models.TextField()
    # 作者
    author = models.CharField(max_length=255)
    # 标签
    tags = models.CharField(max_length=1000)
    # 作者出生日期
    author_born_date = models.CharField(max_length=1000)
    # 作者出生地址
    author_born_location = models.CharField(max_length=1000)
    # 作者介绍
    author_description = models.TextField()
