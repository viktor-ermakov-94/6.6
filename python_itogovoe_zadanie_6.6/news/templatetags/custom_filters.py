from django import template

register = template.Library()

stop_words = [
    'курение',
    'алкоголь',
    'травка',
]


# Теперь каждый раз, когда мы захотим пользоваться нашими фильтрами, в шаблоне нужно будет прописывать следующий тег:
# {% load custom_filters %}

# регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
@register.filter(name='censor')
# первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра,
# т. е. в шаблоне будет примерно следующее - value|multiply:arg
def censor(value):
    # фильтр заменяет слова из стоп-листа на '...'
    for sw in stop_words:
        value = value.lower().replace(sw.lower(), '...')
    return value

    # проверка типов аргументов
    # if isinstance(value, str)
    #     return ...
    # else:
    #     #  в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку
    #     raise ValueError(f'Ошибка! Тип {type(value)} не подходит!')


@register.filter(name='preview')
# первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра,
# т. е. в шаблоне будет примерно следующее - value|multiply:arg
def preview(value):
    if len(value) > 50:
        return value[:51] + '...'
    else:
        return value


if __name__ == '__main__':
    print(censor("""Слово1 слово2 плохое_слово1 Плохое_слово2
плохое_слово3 плохое_слово4 слово3"""))
