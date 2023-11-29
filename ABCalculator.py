# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

# Добавление метки заголовка
lblTitle = tk.Label(text = "A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#000066')
lblTitle.place(x=50, y=20)

#Добавление кнопки "Рассчитать"
btnClose = tk.Button(root, text="Рассчитать", font = ('Helvetica', 10, 'bold'))
btnClose.place(x=25, y=250, width=90, height=30)

#Добавление кнопки закрытия программы
btnClose = tk.Button(root, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

# Запуск цикла mainloop
root.mainloop()
