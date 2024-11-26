from django.db import models

# Create your models here.

from django.db import models
class BlogPost(models.Model):
    CATEGORY = (('OPRPG','オープンRPGゲーム'),
                ('FPS','FPS系ゲーム'),
                ('ターン制','ターン制のゲーム'))
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )
    content = models.TextField(
        verbose_name='本文'
    )
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )
    def __str__(self):
        return self.title
    
