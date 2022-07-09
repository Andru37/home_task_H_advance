def find_uniq(dataset: list) -> int:
    """Берем нулевое значение в списке . Присваеваем переменной и проверяем на наличие копии.
    Удаляем при нахождениии оба значения. Когда в списке останется только одно , мы не сможем войти в цикл.
    оно и будет искомым значением."""
    while len(dataset) > 1:
        first_number = dataset[0]
        for j in dataset:
            if j == first_number:
                dataset.remove(j)
                dataset.remove(j)
    return dataset[0]


c = find_uniq([1, 1, 2, 2, 3, 3, 4, 4, 5])
print(c)


# find_uniq([1, 2, 3, 2, 1]) -> 3
# find_uniq([54, 90, 52, 10, 62, 54, 90, 52, 10, 62, 42]) -> 42

def find_uniq1(dataset: list) -> int:
    """Решение без методов списков. Создаем счетчик количества чисел в списке. Когда найдем
    уникальное число выходим из цикла. """
    n = 0
    while True:
        i = dataset[n]
        a = 0
        for j in dataset:
            if i == j:
                a += 1
        if a == 2:
            n += 1
        else:
            return i


b = find_uniq1([1, 1, 2, 3, 3])
print(b)
