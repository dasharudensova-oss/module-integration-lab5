from input_module import input_array
from processing import is_same_sign
from output import print_result

def main():
    results = []
    for i in range(1, 6):
        print(f"\n--- Массив №{i} ---")
        arr = input_array(5)
        results.append(is_same_sign(arr))
        print_result(i, results[-1])

    found = [i + 1 for i, ok in enumerate(results) if ok]
    if found:
        print(f"\nМассивы одного знака: {found}")
    else:
        print("\nОтрицательный ответ: массивов одного знака нет.")

if __name__ == "__main__":
    main()
