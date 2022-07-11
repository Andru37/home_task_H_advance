from typing import Any, Dict, List


def filter_by_first_met_value(
        dataset: List[Dict[str, Any]], keys: List[str]
) -> List[Dict[str, Any]]:
    """Filter dataset by first met value in keys"""
    list_result: list = []  # Пустой список Бв котором будут уникальные словари
    list_unique_value: list = []  # Пустой список в котором будут уникальные значения
    for next_dict in dataset:  # Итерируемся по списку из условия
        my_value_base: list = [value for key, value in next_dict.items() if key in keys]  # оздаем текущий список значений из словаря
        if my_value_base not in list_unique_value and next_dict not in list_result:  # Делаем проверку и если необходимо добавляем словарь в список
            list_result.append(next_dict)
            list_unique_value.append(my_value_base)
    return list_result


origin = [
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
    {"foo": "F", "bar": "BAR", "foobar": "fb"},
    {"foo": "FOO", "bar": "BAR", "foobar": "fb"},
]
origin1 = [
    {"name": "Serhii"},
    {"name": "Vlad"},
    {"name": "Vlad"},
    {"name": "Vlad"},
    {"name": "Serhii"},
]
print(filter_by_first_met_value(origin, ["foo", "bar"]))
print(filter_by_first_met_value(origin, ["foo"]))
print(filter_by_first_met_value(origin, ["foobar"]))
print(filter_by_first_met_value(origin, ["bar"]))
print(filter_by_first_met_value(origin, ["foo", "bar", "foobar"]))
print(filter_by_first_met_value(origin1, ["name"]))