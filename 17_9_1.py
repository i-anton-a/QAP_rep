def bin_search(element, array_alt, left, right):
    if left > right:
        return False
    middle = (left + right) // 2
    if array_alt[middle] == element:
        return middle
    elif element < array_alt[middle]:
        return bin_search(element, array_alt, left, middle-1)
    else:
        return bin_search(element, array_alt, middle+1, right)

def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array

array = list(map(int, input("введите любую последоватьельность чисел через пробел: ").split()))
element = int(input("Введите любое число которое будем искать: "))

while element:
    if element <= min(array):
        print("Введенное число не соответствует критериям поиска, введите число больше минимального знаечения числа в списке")
        element = int(input("Введите любое число которое будем искать: "))
    elif element > max(array):
        print("Введенное число не соответствует критериям поиска, введите число меньше максимального знаечения числа в списке")
        element = int(input("Введите любое число которое будем искать: "))
    else:
        break

array_alt = sort(array)
print(bin_search(element, array_alt, 0, len(array_alt)-1))
