import tkinter as tk
from tkinter import ttk

from utilities.file_utl import image_to_icon
from settings import ICON_CANCEL, ICON_OK


class EditWindow(tk.Toplevel):
    """ Класс: Окна редактирования записи """

    def __init__(self, parent, exercise, weight, repetitions):
        super().__init__(parent)

        self.exercise = exercise
        self.weight = weight
        self.repetitions = repetitions

        self.title("Редактировать запись")
        self.columnconfigure(1, weight=1)

        self.icon_ok = image_to_icon(ICON_OK)
        self.icon_cancel = image_to_icon(ICON_CANCEL)

        self.exercise_label = ttk.Label(self, text="Упражнение:")
        self.exercise_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        self.exercise_entry = ttk.Entry(self)
        self.exercise_entry.insert(0, self.exercise)
        self.exercise_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        self.weight_label = ttk.Label(self, text="Вес:")
        self.weight_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        validate = self.register(self._validate_digit_input)
        self.weight_entry = ttk.Entry(self, validate="key", validatecommand=(validate, '%P'))
        self.weight_entry.insert(0, self.weight)
        self.weight_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.repetitions_label = ttk.Label(self, text="Повторения:")
        self.repetitions_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        self.repetitions_entry = ttk.Entry(self, validate="key", validatecommand=(validate, '%P'))
        self.repetitions_entry.insert(0, self.repetitions)
        self.repetitions_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

        self.add_button = ttk.Button(self, text="ОК ", command=self.on_button_click,
                                     image=self.icon_ok, compound=tk.LEFT)
        self.add_button.grid(column=0, row=4, pady=5, padx=10)

        # Определим нажатие клавиши Enter как событие "Добавить запись"
        self.bind('<Return>', self.on_button_click)

        self.add_button = ttk.Button(self, text="Отмена ", command=self.cancel_button_click,
                                     image=self.icon_cancel, compound=tk.LEFT)
        self.add_button.grid(column=1, row=4, pady=5, padx=10)

        self.protocol("WM_DELETE_WINDOW", self.cancel_button_click)

        # Рассчитываем середину экрана
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 320) / 2)
        y = int((screen_height - 250) / 2)
        self.geometry(f'320x140+{x}+{y}')

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

    def on_button_click(self, event=None):
        """ Нажата клавиша <ОК> """
        self.exercise = self.exercise_entry.get()
        self.weight = self.weight_entry.get()
        self.repetitions = self.repetitions_entry.get()
        self.destroy()

    def cancel_button_click(self):
        """ Нажата клавиша <Отмена> """
        self.exercise = None
        self.weight = None
        self.repetitions = None
        self.destroy()

    def get_selected_dates(self) -> tuple[str | None, str | None, str | None]:
        """ Получить сохраненные данные после закрытия окна """
        try:
            return self.exercise, self.weight, self.repetitions
        except AttributeError:
            return None, None, None
