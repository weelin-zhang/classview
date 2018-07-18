from django.contrib import admin
from .models import TopLine, BusinessLine, Project, Deployment
# Register your models here.



class TopLineAdmin(admin.ModelAdmin):
    list_display = ("name", "owner",)


class BusinessLineAdmin (admin.ModelAdmin):
    list_display = ("name", "owner", "topline",)
    list_filter = ("name",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "businessline",)
    search_fields = ("owner", "businessline",)

class DeploymentAdmin(admin.ModelAdmin):
    list_display = ("name", "project",)
    search_fields = ("project",)
    
    
admin.site.register(TopLine, TopLineAdmin)
admin.site.register(BusinessLine, BusinessLineAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Deployment, DeploymentAdmin)
