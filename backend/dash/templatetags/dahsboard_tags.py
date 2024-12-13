from django import template

register = template.Library()


@register.simple_tag
def sample_chart_data():
    return [
        {"label": "Category 1", "value": 10},
        {"label": "Category 2", "value": 15},
        {"label": "Category 3", "value": 5},
    ]
