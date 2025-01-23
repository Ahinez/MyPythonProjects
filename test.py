import tkinter as tk

root = tk.Tk()

label_text = tk.StringVar()
label = tk.Label(textvariable=label_text)
label.pack()

def update():
    text = label_text.get()
    if not text:
        text = 'base'
    else:
        text += '.'
    label_text.set(text)

b = tk.Button(root, text='update', command=update)
b.pack()

root.mainloop()