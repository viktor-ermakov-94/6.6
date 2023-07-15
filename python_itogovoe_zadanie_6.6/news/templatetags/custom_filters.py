from django import template

register = template.Library()


bad_words = ['идиот', 'дурак']

@register.filter() 
def censor(value):
    for bw in bad_words:
        value = value.lower().replace(bw.lower(), '*')
    return value


