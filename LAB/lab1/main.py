import sys
import math

def get_coefficient(name: str) -> float:
    """Запрашивает у пользователя ввод коэффициента."""
    while True:
        try:
            return float(input(f"Введите коэффициент {name}: "))
        except ValueError:
            print("Ошибка. Введите действительное число.")

def read_coefficient(index: int, name: str) -> float:
    """Читает коэффициент из аргументов командной строки или запрашивает у пользователя."""
    try:
        return float(sys.argv[index])
    except (IndexError, ValueError):
        return get_coefficient(name)

def get_coefficients() -> tuple[float, float, float]:
    """Получает коэффициенты A, B и C."""
    a = read_coefficient(1, "A")
    b = read_coefficient(2, "B")
    c = read_coefficient(3, "C")
    return a, b, c

def calculate_roots(a: float, b: float, c: float) -> list[float]:
    """Вычисляет корни квадратного уравнения."""
    if a == 0:
        if b == 0:
            return []
        return [-c / b]
    
    discriminant = b * b - 4 * a * c
    print(f"Дискриминант: {discriminant}")
    
    roots = []
    
    if discriminant > 0:
        sqrt_d = math.sqrt(discriminant)
        roots.append((-b + sqrt_d) / (2 * a))
        roots.append((-b - sqrt_d) / (2 * a))
    elif discriminant == 0:
        roots.append(-b / (2 * a))
    
    # Возвращаем корни с учетом извлечения квадратного корня
    result = []
    for root in roots:
        if root > 0:
            result.extend([math.sqrt(root), -math.sqrt(root)])
        elif root == 0:
            result.append(0)
    
    return sorted(result)

def display_roots(roots: list[float]):
    """Выводит корни на экран."""
    count = len(roots)
    if count == 0:
        print("Нет корней.")
    else:
        print(f"{count} {'корень' if count == 1 else 'корня'}: {', '.join(map(str, roots))}")

def main():
    """Главная функция программы."""
    a, b, c = get_coefficients()
    roots = calculate_roots(a, b, c)
    display_roots(roots)

if __name__ == "__main__":
    main()
