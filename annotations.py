from typing import Optional


# Аннотируем параметр функции: "значение name должно быть типа str!"
def we_crash_all(name: Optional[str] = 'Nastya'):
    """
    Метод для объединения строк

    :param name: строка
    """
    return f'Привет, {name}, мы всё сломали!'


name: Optional[str] = 'Ivan'
print(we_crash_all())
