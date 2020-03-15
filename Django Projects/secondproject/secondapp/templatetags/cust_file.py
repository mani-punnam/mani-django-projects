from django import template


register=template.Library()

@register.filter(name='truncate')
def trunc(value,s):
    n1,n2=[int(x) for x in s.split()]
    return value[n1:n2]
