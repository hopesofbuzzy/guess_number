from math import sqrt
from typing import Optional


def add_numbers(num1: float, num2: float) -> float:
    return num1 + num2


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number <= 0:
        return None

    square_root: float = calculate_square_root(your_number)
    return (
        'Мы вычислили квадратный корень из введённого вами числа. '
        f'Это будет: {square_root}'
    )


number1: float = 10
number2: float = 5

print('Сумма чисел: ', add_numbers(number1, number2))
print(calc(25.5))
