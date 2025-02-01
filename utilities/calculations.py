# Функции калькуляции

def difference_values(val_list: list) -> list:
    """
    Разница значений.
    :param val_list: Список значений.
    :return: Список изменений.
    """
    try:
        rez = [None]
        for i in range(len(val_list)-1):
            rez.append(val_list[i] - val_list[i+1])
        return rez
    except Exception:
        return []


def absolut_change(val_list: list) -> float:
    """
    Абсолютное изменение с начала периода.
    :param val_list: Список значений.
    :return: Абсолютное изменение.
    """
    try:
        return val_list[0] - val_list[-1]
    except Exception:
        return 0


def relative_change(val_list: list) -> float:
    """
    Относительное изменение с начала периода в процентах.
    :param val_list: Список значений.
    :return: Относительное изменение в процентах.
    """
    try:
        return (val_list[0] - val_list[-1]) / val_list[0] * 100
    except Exception:
        return 0
