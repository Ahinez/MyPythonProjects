import tkinter as tk
from tkinter import messagebox

def toggle_window():
    if checkbox_var.get():
        # Если чекбокс активирован, создаем новое окно
        new_window = tk.Toplevel(root)
        new_window.title("Новое окно")
        
        # Создаем кнопку в новом окне
        button = tk.Button(new_window, text="Нажми меня", command=on_button_click)
        button.pack(pady=20)
    else:
        # Если чекбокс деактивирован, закрываем все открытые окна
        for window in root.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()

def on_button_click():
    messagebox.showinfo("Информация", "Кнопка нажата!")

# Основное окно
root = tk.Tk()
root.title("Основное окно")

# Переменная для чекбокса
checkbox_var = tk.BooleanVar()

# Создаем чекбокс
checkbox = tk.Checkbutton(root, text="Открыть новое окно", variable=checkbox_var, command=toggle_window)
checkbox.pack(pady=20)

# Запускаем главный цикл приложения
root.mainloop()