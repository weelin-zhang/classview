from django import template
register = template.Library()

@register.filter
def line_str_of_topuser(user):
    return ''.join(line.name for line in user.toplines.all())

@register.filter
def line_str_of_businesslineuser(user):
    return ''.join(line.name for line in user.businesslines.all())
