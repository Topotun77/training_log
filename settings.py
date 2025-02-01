# Настройки приложения

from utilities.stat import (stat_weight_reduce, stat_relative_weight, stat_count_training,
                            stat_count_in_day, stat_average_weight_loss)

# Файл для сохранения данных
data_file = 'data/training_log.json'
# data_file = 'data/training_log.csv'

# Формат файла ввода/вывода данных ('JSON', 'CSV')
file_format = data_file.split('.')[-1]
# file_format = 'json'
# file_format = 'csv'

# Файлы иконок
ICON_VIEW = './icon/view.png'
ICON_ADD = './icon/add.png'
ICON_CHART = './icon/chart.png'
ICON_OK = './icon/ok.png'
ICON_CANCEL = './icon/cancel.png'
ICON_EDIT = './icon/edit.png'

# Текст вывода статистики. Настройка производится в формате списка списков:
# [['Текст до параметра', <функция для вычисления>, 'Текст после параметра'], ...]
# В функцию передаются данные в виде списка словарей с данными. Возвращает функция строку.
# Можно использовать функции из модуля utilities.stat
STATISTIC = [
    [
        'Ниже приведены Ваши успехи за выбранный период и с учетом фильтрации. '
        'Обратите внимание, что отрицательные значения будут означать прибавку веса.\n\n'
        'Ваше снижение веса составило: ',
        stat_weight_reduce,
        ' кг.\n'
    ],
    [
        'Ваше относительное снижение веса составило: ',
        stat_relative_weight,
        ' %\n'
    ],
    [
        'Всего количество тренировок за период: ',
        stat_count_training,
        '\n'
    ],
    [
        'Среднее количество тренировок в день: ',
        stat_count_in_day,
        '\n'
    ],
    [
        'Средняя потеря веса за одну тренировку: ',
        stat_average_weight_loss,
        'кг.\n'
    ],
]