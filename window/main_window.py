from tkinter import ttk, messagebox
import tkinter as tk

from tkcalendar import DateEntry

from utilities.file_utl import image_to_icon, load_data, save_data, load_data_filter
from utilities.charts import create_any_plot
from settings import ICON_VIEW, ICON_CHART, ICON_ADD, STATISTIC
from window.select_dare_period import DateSelectionWindow
from window.training_grid import ToplevelGrid


class DateTimePicker(ttk.Frame):
    """ Класс календарь со временем """

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.date_entry = DateEntry(self, width=10, bg='darkblue', fg='white', borderwidth=3, relief='ridge',
                                    locale='ru', date_pattern='dd.mm.y')
        self.date_entry.pack(side=tk.LEFT, padx=10, pady=5)

        validate = self.master.register(self._validate_digit_input)
        self.hour_spin = ttk.Spinbox(self, from_=0, to=23, width=5, format='%02.0f', validate="key",
                                     validatecommand=(validate, '%P'))
        self.hour_spin.pack(side=tk.LEFT, padx=0, pady=5)

        self.minute_spin = ttk.Spinbox(self, from_=0, to=59, width=5, format='%02.0f', validate="key",
                                     validatecommand=(validate, '%P'))
        self.minute_spin.pack(side=tk.LEFT, padx=0, pady=5)

    def get(self):
        """ Возвращает значения полей календаря с часами """
        date_str = self.date_entry.get_date()
        hour_spin=self.hour_spin.get()
        minute_spin=self.minute_spin.get()
        if hour_spin.isdigit():
            hour_spin = int(hour_spin) % 24
        else:
            hour_spin = 0
        if minute_spin.isdigit():
            minute_spin = int(minute_spin) % 60
        else:
            minute_spin = 0
        time_str = f'{hour_spin:02}:{minute_spin:02}'
        return f'{date_str} {time_str}'

    def _validate_digit_input(self, new_value: str) -> bool:
        """ Метод для валидации ввода значения в поле времени. Ввести можно только цифры """
        if new_value == "" or new_value.isdigit():
            return True
        else:
            return False


class TrainingLogApp(tk.Tk):
    """ Основное окно приложения """

    def __init__(self):
        super().__init__()
        self.title("Дневник тренировок")
        self.minsize(320, 310)
        self.resizable(width=True, height=False)

        self.create_widgets()

    def create_widgets(self):
        """ Виджеты для ввода данных """
        self.icon_view = image_to_icon(ICON_VIEW)
        self.icon_chart = image_to_icon(ICON_CHART)
        self.icon_add = image_to_icon(ICON_ADD)

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
        self.main_frame.columnconfigure(1, weight=1)

        self.date_time = DateTimePicker(self.main_frame)
        self.date_time.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)

        self.exercise_label = ttk.Label(self.main_frame, text="Упражнение:")
        self.exercise_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.exercise_entry = ttk.Entry(self.main_frame)
        self.exercise_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        self.weight_label = ttk.Label(self.main_frame, text="Вес:")
        self.weight_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        validate = self.main_frame.register(self._validate_digit_input)
        self.weight_entry = ttk.Entry(self.main_frame, validate="key", validatecommand=(validate, '%P'))
        self.weight_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.repetitions_label = ttk.Label(self.main_frame, text="Повторения:")
        self.repetitions_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        self.repetitions_entry = ttk.Entry(self.main_frame, validate="key", validatecommand=(validate, '%P'))
        self.repetitions_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        self.add_button = ttk.Button(self.main_frame, text="Добавить запись ", command=self.add_entry,
                                     image=self.icon_add, compound=tk.LEFT)
        self.add_button.grid(column=0, row=4, columnspan=2, pady=5, padx=10)

        self.frame_view = tk.Frame(self.main_frame)
        self.frame_view.grid(row=5, column=0, columnspan=2, pady=1)

        self.view_button = ttk.Button(self.frame_view, text="Просмотреть всё ", command=self.view_records,
                                      image=self.icon_view, compound=tk.LEFT)
        self.view_button.grid(column=0, row=0, pady=5, padx=5)

        self.view_button = ttk.Button(self.frame_view, text="Отфильтровать записи ", command=self.view_records_filter,
                                      image=self.icon_view, compound=tk.LEFT)
        self.view_button.grid(column=1, row=0, pady=5, padx=5)

        self.view_button = ttk.Button(self.main_frame, text="Посмотреть статистику с фильтром ",
                                      command=self.view_statistics,
                                      image=self.icon_chart, compound=tk.LEFT)
        self.view_button.grid(column=0, row=6, columnspan=2, pady=5, padx=5)

        self.view_button = ttk.Button(self.main_frame, text="Построить графики с фильтром ",
                                      command=self.plot_chart,
                                      image=self.icon_chart, compound=tk.LEFT)
        self.view_button.grid(column=0, row=7, columnspan=2, pady=5, padx=5)

        # Рассчитываем середину экрана
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 320) / 2)
        y = int((screen_height - 250) / 2)
        # self.geometry('%dx%d+%d+%d' % (220, 100, x, y))
        self.geometry(self.geometry().split('+')[0] + f'+{x}+{y}')

    def _validate_digit_input(self, new_value: str) -> bool:
        """
        Метод для валидации ввода дробных значений. Ввести можно только число
        """
        if new_value == '':
            return True
        try:
            float(new_value)
            return True
        except ValueError:
            return False

    def add_entry(self):
        """
        Добавление записи в журнал (json-файл)
        """
        date = self.date_time.get()
        exercise = self.exercise_entry.get()
        weight = self.weight_entry.get()
        repetitions = self.repetitions_entry.get()

        if not (exercise and weight and repetitions):
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return

        entry = {
            'date': date,
            'exercise': exercise,
            'weight': weight,
            'repetitions': repetitions
        }
        data = load_data()
        data.append(entry)
        rez = save_data(data)

        # Очистка полей ввода после добавления
        self.exercise_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.repetitions_entry.delete(0, tk.END)
        if rez:
            messagebox.showinfo("Успешно", "Запись успешно добавлена!")

    def get_filter_data(self):
        """ Получить фильтрованные данные за период """

        # Получаем даты начала и конца периода
        date_selection_window = DateSelectionWindow(self)
        self.wait_window(date_selection_window)
        start_date, end_date = date_selection_window.get_selected_dates()

        # Взять данные из формы
        exercise = self.exercise_entry.get()
        weight = self.weight_entry.get()
        repetitions = self.repetitions_entry.get()

        # Сохраняем в словарь
        filter_ = {
            'exercise': exercise,
            'weight': weight,
            'repetitions': repetitions,
            'start_date': start_date,
            'end_date': end_date,
        }
        return load_data_filter(filter_)

    def view_records(self):
        """ Просмотр записей журнала тренировок в отдельном окне """
        data = load_data()
        ToplevelGrid(self, data)

    def view_records_filter(self):
        """ Просмотр записей журнала тренировок в отдельном окне с фильтрацией записей """
        data = self.get_filter_data()
        ToplevelGrid(self, data)

    def view_statistics(self):
        """ Отображение статистики. Настраивается через файл настроек settings.py """
        data = self.get_filter_data()
        if not data:
            messagebox.showerror('Нет данных', 'Нет данных для вывода статистики. '
                                               'Измените фильтр для отбора записей.')
            return
        stat = ''
        for item in STATISTIC:
            stat += item[0] + item[1](data) + item[2] + '\n'
        messagebox.showinfo("Статистика", stat)

    def plot_chart(self):
        """ Визуализация данных """
        data = self.get_filter_data()
        create_any_plot(data)
