from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True)

    # 修改数据显示名称
    def __str__(self):
        return self.title
