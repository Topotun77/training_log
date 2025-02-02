import tkinter as tk
from tkinter import ttk

from tkcalendar import DateEntry

from utilities.file_utl import image_to_icon
from settings import ICON_CANCEL, ICON_OK


class DateSelectionWindow(tk.Toplevel):
    """ Класс окна выбора периода дат """

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Выбор периода")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 265) / 2)
        y = int((screen_height - 136) / 2)
        self.geometry('%dx%d+%d+%d' % (265, 136, x, y))
        self.resizable(False, False)

        self.label_info = ttk.Label(self, text='<Отмена> - фильтрация без учета дат.')
        self.label_start_date = tk.Label(self, text="Начальная дата:")
        self.label_end_date = tk.Label(self, text="Конечная дата:")
        self.date_entry_start = DateEntry(self, width=10, bg='darkblue', fg='white', borderwidth=3, relief='ridge',
                                    locale='ru', date_pattern='dd.mm.y')
        self.date_entry_end = DateEntry(self, width=10, bg='darkblue', fg='white', borderwidth=3, relief='ridge',
                                    locale='ru', date_pattern='dd.mm.y')

        self.icon_cancel = image_to_icon(ICON_CANCEL)
        self.icon_ok = image_to_icon(ICON_OK)

        self.button_ok = ttk.Button(
            self,
            text="Выбрать период",
            command=lambda: self.on_button_click(parent),
            image=self.icon_ok,
            compound = tk.LEFT
        )
        self.button_cancel = ttk.Button(
            self,
            text="Отмена",
            command=lambda: self.cancel_button_click(parent),
            image=self.icon_cancel,
            compound=tk.LEFT
        )
        # Определим нажатие клавиши Enter как событие "Добавить запись"
        self.bind('<Return>', self.on_button_click)

        self.label_info.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky=tk.W)
        self.label_start_date.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.date_entry_start.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.label_end_date.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.date_entry_end.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.button_ok.grid(row=3, padx=10, column=0, pady=5)
        self.button_cancel.grid(row=3, padx=10, column=1, pady=5)

    def on_button_click(self, parent=None):
        """ Нажата кнопка <ОК> """
        self.selected_start_date = self.date_entry_start.get_date()
        self.selected_end_date = self.date_entry_end.get_date()
        self.destroy()

    def cancel_button_click(self, parent=None):
        """ Нажата кнопка <Отмена> """
        self.selected_start_date = None
        self.selected_end_date = None
        self.destroy()

    def get_selected_dates(self):
        """ Получить сохраненные данные после закрытия окна """
        try:
            return self.selected_start_date, self.selected_end_date
        except AttributeError:
            return None, None
