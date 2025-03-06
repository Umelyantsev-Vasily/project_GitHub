import re

from masks import get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция которая маскирует номер счета/карты"""
    str_slit = string.split()
    name_card = " ".join(str_slit[:-1])
    number_card = str_slit[-1]
    return name_card, number_card


# Проверяем функцию
test = "Visa Platinum 7000792289606361"
name, number = mask_account_card(test)
mask_number = get_mask_card_number(number)
print(f"{name}, {mask_number}")


def get_date(input_str: str) -> str:
    """Функция которая преобразует дату и выводит"""
    data_title = ""
    for items in input_str:
        cler_str = re.findall("[0-9]", items)
        if cler_str:
            data_title += "".join(cler_str)
    return f"{data_title[6:8]}.{data_title[4:6]}.{data_title[0:4]}"


# Проверяем вторую функцию
test2 = "2024-03-11T02:26:18.671407"
print(get_date(test2))
