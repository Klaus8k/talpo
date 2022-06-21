from django import template
# здесь размещаем пользвовательские теги для шаблонов

register = template.Library()

# with decorator @register.simple_tag() call func to our template tag
