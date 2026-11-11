def input_array(n):
    arr = []
    print(f"Введите {n} вещественных чисел через пробел:")
    while len(arr) < n:
        try:
            parts = input().split()
            arr.extend(float(x) for x in parts)
        except ValueError:
            print("Ошибка: введите числа.")
    return arr[:n]