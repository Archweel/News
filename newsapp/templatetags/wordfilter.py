from django import template

register = template.Library()

BAD_LIST = [
    'мат',
    'мат',
    'мат',
]
@register.filter(name='censor')
def censor(value):
    if isinstance(value, str):
        for word in BAD_LIST:
            result = value.replace(word, "****")
        return result





