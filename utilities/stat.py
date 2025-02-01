# Библиотека с функциями для формирования статистического отчета.
# Все функции получают на входе данные в виде списка словарей, а на выходе выдают строку
from datetime import datetime

from .calculations import absolut_change, relative_change


def stat_weight_reduce(data) -> str:
    """
    Выдает абсолютное изменение (снижение) веса за весь период.
    Отрицательное значение означает прибавку веса.
    """
    wg_list = [float(x['weight']) for x in data]
    return str(round(absolut_change(wg_list), 1))


def stat_relative_weight(data) -> str:
    """
    Выдает относительное изменение (снижение) веса за весь период.
    Отрицательное значение означает прибавку веса.
    """
    wg_list = [float(x['weight']) for x in data]
    return str(round(relative_change(wg_list), 1))


def stat_count_training(data) -> str:
    """
    Количество тренировок за выбранный период
    """
    return str(len(data))


def stat_count_in_day(data) -> str:
    """
    Среднее количество тренировок в день
    """
    dt_list = [datetime.strptime(x['date'], '%Y-%m-%d %H:%M') for x in data]
    # Дельта в днях
    day = max((dt_list[-1] - dt_list[0]).days, 1)
    return str(round(len(data) / day, 2))


def stat_average_weight_loss(data) -> str:
    """
    Средняя потеря веса на одну тренировку
    """
    wg_list = [float(x['weight']) for x in data]
    return str(round(absolut_change(wg_list)/len(wg_list), 3))
