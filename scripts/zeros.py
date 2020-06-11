def get_zeros(n: int) -> int:
    """Получить количество нулей в конце n!"""
    count = 0
    if n > 0:
        str_factorial = str(calculate_factorial(n))
        for digit in reversed(str_factorial):
            if digit != '0':
                break
            count += 1
    return count


def calculate_factorial(n: int) -> int:
    """Функция для расчета факториала"""
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
