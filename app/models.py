from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(verbose_name="作者姓名", max_length=20, unique=True)
   
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    name = models.CharField(verbose_name="书名", max_length=64, unique=True)
    price = models.DecimalField(verbose_name="价格", max_digits=7, decimal_places=2)
    author = models.ForeignKey(Author, verbose_name="作者", related_name="books")
