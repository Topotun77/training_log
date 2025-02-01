from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import pylab
from .calculations import difference_values


def create_any_plot(data):
    """
    Построение графиков на основе данных
    :param data: Данные в виде списка словарей
    """
    plt.figure(figsize=(8, 8))
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title(f'Динамика изменения веса')

    # Считать данные
    dt_list = [datetime.strptime(x['date'], '%Y-%m-%d %H:%M') for x in data]
    wg_list = [float(x['weight']) for x in data]
    re_list = [int(x['repetitions']) for x in data]
    ex_list = [str(x['exercise']) for x in data]
    dif_list = difference_values(wg_list)

    # Строим первый график
    ax1 = plt.subplot2grid(shape=(15, 10), loc=(0, 0), rowspan=5, colspan=10)
    ax1.plot(dt_list, wg_list, label='Вес', linewidth=0.8, color='red')
    ax1.set_title('Динамика снижения веса')
    ax1.set_ylabel('Вес')
    ax1.legend()

    # Строим второй график
    ax2 = plt.subplot2grid(shape=(15, 10), loc=(6, 0), rowspan=3, colspan=10)
    ax2.plot(dt_list, dif_list, label='Снижение веса', linewidth=0.8)
    # Отмечаем нулевую линию
    ax2.axhline(0, color='red', linestyle='--', linewidth=1)
    ax2.set_title('Изменение веса (снижение)')
    ax2.set_ylabel('Снижение веса')
    ax2.legend()

    # Строим третий график
    ax3 = plt.subplot2grid(shape=(15, 10), loc=(10, 0), rowspan=5, colspan=10)
    ax3.bar(dt_list, re_list, label='Повторения', width=0.1, color='#00b0ff')
    for i in range(len(dt_list)):
        ax3.text(dt_list[i], re_list[i], ex_list[i], ha='center', va='top', rotation=70)
    ax3.set_title('Количество повторов упражнений')
    ax3.set_xlabel('Дата')
    ax3.set_ylabel('Повторы')
    ax3.legend()

    plt.tight_layout()
    plt.show()
