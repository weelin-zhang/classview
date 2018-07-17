from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    
    # 自定义以权限
    class Meta:
        permissions = (
            ("favor_post", "give favor post"),
        )
        
    def __str__(self):
        return self.title
