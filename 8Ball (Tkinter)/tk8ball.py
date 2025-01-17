import tkinter as tk
from tkinter import ttk

def Exit():
    root.destroy()

def Send():
    print('Ты нажал на кнопку "Send"')

root = tk.Tk()

root.title('8Ball')

root.iconbitmap('E:\Projects\MyPyhtonProjects\8Ball (Tkinter)\8ball.ico')

root.geometry('800x500+600+300')
root.resizable(False, False)

label = tk.Label(root, text="Ask your question", font=('Roboto Mono Light', 18))
label.pack(padx=20, pady=20)

textbox =tk.Text(root, height=1, font=('Roboto Mono Light', 16))
textbox.pack(side='bottom', padx=[10, 100], pady=10)

sendbtn = ttk.Button(root, text='Send', command=Send)
sendbtn.place(x=710, y=458, height=32)

# Send and Exit buttons
# btn = ttk.Button(text='Send', command=Send)
# btn.place(relx=0.88, rely=0.85) # btn.pack(expand=True, anchor=SE, padx=10)
# btn = ttk.Button(text='Exit', command=Exit)
# btn.place(relx=0.88, rely=0.90) # btn.pack(anchor=SE, padx=10, pady=[0, 10])

root.mainloop()