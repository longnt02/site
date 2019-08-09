from django.template.loader import get_template
from django import template

register = template.Library()

@register.simple_tag()
def get_header():
    return get_template('polls/header.html').render()

@register.simple_tag
def get_sidebar():
    return get_template('polls/sidebar.html').render()

@register.simple_tag
def get_footer():
    return get_template('polls/footer.html').render()


