import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(text='Enter something')
label.grid(row=0, column=0)

entry = ttk.Entry()
entry.grid(row=0, column=1)

root.mainloop()