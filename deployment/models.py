from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TopLine(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="顶级业务线")
    owner= models.ForeignKey(User, related_name="toplines", verbose_name="业务线leader")
    
    class Meta:
        verbose_name_plural = "顶级业务线"
    
    def __str__(self):
        return self.name
    
    
class BusinessLine(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="次级业务线")
    owner = models.ForeignKey(User, related_name="businesslines", verbose_name="小组leader")
    topline = models.ForeignKey(TopLine, related_name="businesslines", verbose_name="顶级业务线")
    
    class Meta:
        verbose_name_plural = "业务小组"
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    '''
    owner是业务小组的leader, 并没有分配给普通的研发人员
    '''
    name = models.CharField(max_length=64, unique=True, verbose_name="项目")
    owner = models.ForeignKey(User, related_name="projects", verbose_name="项目负责人")
    businessline = models.ForeignKey(BusinessLine, related_name="projects", verbose_name="所属业务线")
    
    class Meta:
        verbose_name_plural = "项目"

        permissions = [
            ("deploy_project", "deploy project"),
        ]
    def __str__(self):
        return self.name
    

class Deployment(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="部署任务")
    project = models.ForeignKey(Project, related_name="deployments")
    
    
    class Meta:
        verbose_name_plural = "发布任务"
        # 最终没用到, 使用preject object permission
        permissions = [
            ("view_deployment", "view deployment"),
        ]
    
    def __str__(self):
        return self.name
    

