# Утилиты для работы с файлами
import csv
import json
from datetime import datetime
from tkinter import messagebox

from PIL import ImageTk, Image
from settings import data_file, file_format


def load_data(fl_format: str = file_format):
    """
    Загрузка данных о тренировках из файла
    :param fl_format: Формат файла ввода/вывода данных ('JSON', 'CVS')
    :return: данные из файла
    """
    if fl_format.lower() == 'json':
        try:
            with open(data_file, 'r', encoding='utf-8') as file:
                return sorted(json.load(file), key=lambda item: item['date'])
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    if fl_format.lower() == 'csv':
        try:
            with open(data_file, 'r', encoding='utf-8') as file:
                data = csv.DictReader(file)
                print(data)
                return [row for row in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []


def load_data_filter(filter_: dict, fl_format: str = file_format):
    """
    Загрузка из файла и фильтрация данных о тренировках
    :param filter_: Словарь фильтров поиска. Формат словаря:
        filter_ = {
            'exercise': Упражнение,
            'weight': Вес,
            'repetitions': Повторения,
            'start_date': Дата начала периода фильтрации,
            'end_date': Дата окончания периода фильтрации,
        }
    :param fl_format: Формат файла ввода/вывода данных ('JSON', 'CVS')
    :return: данные из файла
    """
    data = load_data(fl_format=fl_format)
    data_filter = []
    try:
        for entry in data:
            date = datetime.strptime(entry['date'].split()[0], '%Y-%m-%d').date()
            if (filter_['exercise'].upper() in entry['exercise'].upper()
                    and filter_['weight'].upper() in entry['weight'].upper()
                    and (filter_['repetitions'] == '' or filter_['repetitions'] == entry['repetitions'])
                    and (filter_['start_date'] is None or filter_['end_date'] is None
                         or filter_['start_date'] <= date <= filter_['end_date'])):
                data_filter.append(entry)
        return data_filter
    except Exception as error:
        print(error.args)
        return []


def save_data(data, fl_format: str = file_format) -> bool:
    """
    Сохранение данных о тренировках в файл
    :param data: Данные для вывода в файл
    :param fl_format: Формат файла ввода/вывода данных ('JSON', 'CVS')
    :return: успех/неудача
    """
    if fl_format.lower() == 'json':
        try:
            with open(data_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось записать файл!\n{e.args}")
            return False
    if fl_format.lower() == 'csv':
        try:
            with open(data_file, 'w', newline='', encoding='utf-8') as file:
                fieldnames = [key for key in data[0].keys()]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            return True
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось записать файл!\n{e.args}")
            return False


def delete_data(data_for_del, fl_format: str = file_format) -> bool:
    """
    Удаление элемента из базы
    :param data_for_del: Строка, которую нужно удалить. Формат:
    ['2025-01-30 13:13', 'Жим лежа', 119, 20]
    :param fl_format: Формат файла ввода/вывода данных ('JSON', 'CVS')
    :return: успех/неудача
    """
    data = load_data(fl_format=fl_format)
    for item in data:
        if item['date'] == data_for_del[0]:
            data.remove(item)
    return save_data(data, fl_format=fl_format)


def image_to_icon(file: str, min_x=20, min_y=20):
    """
    Изменение размера картинки для иконки.
    :param file: Имя файла.
    :param min_x: Размер по горизонтали.
    :param min_y: Размер по вертикали.
    :return: Объект ImageTk.PhotoImage.
    """
    try:
        im = Image.open(file)
        im = im.resize((min_x, min_y))
    except:
        return None
    return ImageTk.PhotoImage(im)