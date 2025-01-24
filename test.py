import tkinter as tk

def copy_to_clipboard():
    # Получаем текст из текстового поля
    text = text_entry.get()
    # Очищаем буфер обмена
    root.clipboard_clear()
    # Добавляем текст в буфер обмена
    root.clipboard_append(text)
    # Сообщаем пользователю, что текст скопирован
    status_label.config(text="Текст скопирован в буфер обмена!")

# Создаем главное окно
root = tk.Tk()
root.title("Копирование текста в буфер обмена")

# Создаем текстовое поле для ввода текста
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=10)

# Создаем кнопку для копирования текста
copy_button = tk.Button(root, text="Копировать", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Создаем метку для отображения статуса
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Запускаем главный цикл приложения
root.mainloop()