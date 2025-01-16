from tkinter import *
from tkinter import ttk

def Exit():
    root.destroy()

def Send():
    print('Ты нажал на кнопку "Send"')

root = Tk()

root.title('8Ball')
root.iconbitmap('E:\Projects\MyPyhtonProjects\8Ball (Tkinter)\8ball.ico')
root.geometry('500x500+700+300')

btn = ttk.Button(text='Send', command=Send)
btn.pack(expand=True, anchor=SE, padx=10)

btn = ttk.Button(text='Exit', command=Exit)
btn.pack(anchor=SE, padx=10, pady=[0, 10])

root.mainloop()