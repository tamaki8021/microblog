from django.db import models

# Create your models here.

class Blog(models.Model):
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True) # 自動的に一度だけその時の日時が保存される

    # sort 新しい順に並べる
    class Meta:
        ordering = ['-posted_date']
