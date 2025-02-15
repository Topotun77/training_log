# Журнал тренировок

Данное приложение позволяет вести журнал тренировок: вносить данные, 
просматривать уже имеющиеся данные, осуществлять поиск по различным полям, 
визуализировать результаты.

## История разработки приложения:

- Добавлена возможность вносить дату и время тренировки.  
- Добавлена возможность хранить данные в `JSON` или `CSV` формате. Выбор формата осужествояется челез файл настроек.  
- Добавлена фильтрация записей по дате - возможность просматривать записи за определенный период.  
- Добавлена фильтрация записей по упражнению - возможность просматривать записи по конкретному упражнению.  
- Возможность фильтровать записи по любому полю или по комбинации полей и дат.
Условие выбора записи - строка поиска есть содержится в соответствующем поле записи в базе данных.
Т.е., например, строка `жим` содержится в строке `отжимание` и `Жим лежа`.  
- Организован запрет ввода текста в поля, которые предназначены для цифровых значений. Ввод проверяется непосредственно при нажатии клавиши.  
- Добавлен скроллбокс для таблицы.  
- Добавлены кнопки `Редактировать` и `Удалить` в окно с таблицей.  
- Добавлена возможность удаление записей.
- Добавлена возможность редактирования записей.  
- Добавлена визуализация данных на графиках.  
- Добавлен вывод статистики по тренировкам. Статистика может рассчитываться как по всем данным, 
так и по отфильтрованным данным по любому полю/полям и датам. Вывод статистики полностью настраивается
в файле настроек.  
- Добавлена возможность занесения данных в журнал, а также редактирования записей и выбора периода по нажатию клавиши Enter.  


### Скриншот приложения:
![img01](https://github.com/Topotun77/training_log/blob/master/ScreenShots/n001.JPG?raw=true)
### Таблица с данными:
![img02](https://github.com/Topotun77/training_log/blob/master/ScreenShots/n002.JPG?raw=true)
### Редактирование записи:
![img03](https://github.com/Topotun77/training_log/blob/master/ScreenShots/n004.JPG?raw=true)
### Выбор периода расчета:
Используется для фильтрации данных при выводе самих данных, а так же для построения графиков и 
расчета статистики. Для фильтрации данных помимо дат, используются данные из полей ввода.  
![img04](https://github.com/Topotun77/training_log/blob/master/ScreenShots/n005.JPG?raw=true)
### График, построенный по данным:
Также можно построить график по отфильтрованным данным.  
![img05](https://github.com/Topotun77/training_log/blob/master/ScreenShots/n003.JPG?raw=true)
### Статистика по отфильтрованным данным:
![img06](https://github.com/Topotun77/training_log/blob/master/ScreenShots/n006.JPG?raw=true)


## Для запуска приложения:
1. **Установите все необходимые зависимости, выполнив команду:**  
```
pip install -r requirements.txt
```
2. **Произведите настройки в файле [`settings.py`](https://github.com/Topotun77/training_log/blob/master/settings.py).**  
В файле настроек есть подробное описание каждого параметра.

3. **Запустите приложение командой:**
```
python main.py
```
