from django import template
register = template.Library()

# @register.filter
# def user_global_perm_check(user, app_label_codename):
#     此处判断global permisson
#     return user.has_perm(app_label_codename)


@register.filter
def permission_managerment(user):
    try:
        return  user.is_superuser or user.businesslines.all().count() !=0 or user.toplines.all().count()!=0
    except AttributeError:
        return False
