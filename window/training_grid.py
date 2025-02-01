from tkinter import Toplevel, ttk, messagebox

import tkinter as tk

from utilities.file_utl import image_to_icon, delete_data, load_data, save_data
from settings import ICON_CANCEL, ICON_EDIT
from window.edit_window import EditWindow


class ToplevelGrid(Toplevel):
    """ Класс окна вывода информации о тренировках """

    def __init__(self, parent, data: list):
        super().__init__(parent)
        self.title("Записи тренировок")
        self.minsize(300, 200)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.icon_delete = image_to_icon(ICON_CANCEL)
        self.icon_edit = image_to_icon(ICON_EDIT)

        self.edit_button = ttk.Button(self, text="Редактировать ", command=self.edit_records,
                                      image=self.icon_edit, compound=tk.LEFT)
        self.edit_button.grid(column=0, row=0, pady=5, padx=5, sticky=tk.E)

        self.edit_button = ttk.Button(self, text="Удалить", command=self.delete_records,
                                      image=self.icon_delete, compound=tk.LEFT)
        self.edit_button.grid(column=1, row=0, pady=5, padx=5, sticky=tk.E)

        # Вывести данные
        self.read_data(data)


    def read_data(self, data):
        """ Вывод/обновление данных в таблицу """
        self.tree = ttk.Treeview(self, columns=("Дата", "Упражнение", "Вес", "Повторения"), show="headings")
        self.tree.heading('Дата', text="Дата")
        self.tree.heading('Упражнение', text="Упражнение")
        self.tree.heading('Вес', text="Вес")
        self.tree.heading('Повторения', text="Повторения")

        for entry in data:
            self.tree.insert('', tk.END, values=(entry['date'], entry['exercise'], entry['weight'], entry['repetitions']))

        # Создаем скроллбар
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.grid(row=1, column=2, sticky=tk.NSEW)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.grid(column=0, row=1, columnspan=2, pady=5, padx=5, sticky=tk.NSEW)


    def delete_records(self):
        """ Удалить запись """
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Предупреждение", "Сначала выберите запись для удаления.")
            return

        if messagebox.askyesno('Удаление', 'Вы уверены, что хотите удалить эту запись?'):
            # Получить выделенные в таблице данные
            item_for_del = self.tree.item(selected_item)['values']
            rez = delete_data(item_for_del)
            if rez:
                self.tree.delete(selected_item)
                messagebox.showinfo("Успешно", "Запись успешно удалена!")

    def edit_records(self):
        """ Редактировать запись """
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Предупреждение", "Сначала выберите запись для редактирования.")
            return

        item_for_edit = self.tree.item(selected_item)['values']

        # Получить отредактированные данные
        edit_date = EditWindow(self, *item_for_edit[1:])
        self.wait_window(edit_date)
        exercise, weight, repetitions = edit_date.get_selected_dates()

        if exercise is not None and weight is not None and repetitions is not None:
            rez = delete_data(item_for_edit)
            if rez:
                date = item_for_edit[0]

                entry = {
                    'date': date,
                    'exercise': exercise,
                    'weight': weight,
                    'repetitions': repetitions
                }

                data = load_data()
                data.append(entry)
                rez = save_data(data)
                self.tree.delete(selected_item)
                self.read_data(data)

                if rez:
                    messagebox.showinfo("Успешно", "Запись успешно обновлена!")
        else:
            messagebox.showinfo('Отмена', 'Все поля должны быть заполнены! Редактирование отменено!')

