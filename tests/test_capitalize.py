from package_name import capitalize


if capitalize.capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')

if capitalize.capitalize('') != '':
    raise Exception('Функция работает неверно!')


print('Все тесты пройдены!')