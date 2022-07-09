from typing import Any, Dict, List


def filter_by_first_met_value(
        dataset: List[Dict[str, Any]], keys: List[str]
) -> List[Dict[str, Any]]:
    """Filter dataset by first met value in keys"""
    list_result: list = [dataset[0]]  # Создаем список с нулевым элементом списка,взятым из исходного списка
    my_value_base: list = [value for key, value in dataset[0].items() if key in keys]  # Базовый список значений, взятый по ключам из нулегого элемента списка
    for next_dict in dataset[1:]:
        my_value_next: list = [value for key, value in next_dict.items() if key in keys]  # Следующий список значений, созданный для проверки
        if my_value_next == my_value_base:  # Проверка : сдобавлением или без добавления нового члена списка
            continue
        list_result.append(next_dict)
    return list_result


origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]
print(filter_by_first_met_value(origin, ["foo", "bar"]))
print(filter_by_first_met_value(origin, ["foo"]))
print(filter_by_first_met_value(origin, ["foobar"]))
print(filter_by_first_met_value(origin, ["bar"]))
print(filter_by_first_met_value(origin, ["foo", "bar", "foobar"]))
