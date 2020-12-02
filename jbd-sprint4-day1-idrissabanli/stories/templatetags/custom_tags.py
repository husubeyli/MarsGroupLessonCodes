from django.template import Library

register = Library()

# a = '1,2,3,4,5'
# a.split(',') ~ ['1','2','3','4','5']

@register.filter
def split_filter(str_value, split_by):
    return str_value.split(split_by)


navbar_elements = [
    'Home',
    'About',
    'Contact',
    'Services'
]

@register.simple_tag
def get_navbar():
    return navbar_elements