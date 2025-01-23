import tkinter as tk

def create_interface():
    root = tk.Tk()
    root.title("Копируемый текст")

    # Создаем виджет Entry
    entry = tk.Entry(root, width=40)
    entry.insert(0, "Это однострочный текст для копирования.")
    entry.config(state="readonly")  # Делаем его только для чтения
    entry.pack(pady=10)

    root.mainloop()

create_interface()
