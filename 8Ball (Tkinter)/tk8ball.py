import tkinter as tk
from tkinter import ttk

def Exit():
    root.destroy()

def Send():
    print('Ты нажал на кнопку "Send"')

def Output(event):
    print(f'You entered: {entry.get()}')

root = tk.Tk()

root.title('8Ball')

root.iconbitmap('E:\Projects\MyPyhtonProjects\8Ball (Tkinter)\8ball.ico')

root.geometry('800x500+600+300')
root.resizable(False, False)

label = tk.Label(root, text="Ask your question", font=('Roboto Mono Light', 18))
label.pack(padx=20, pady=20)

entry = ttk.Entry(width=125)
entry.pack(side='bottom', pady=10)
entry.bind("<Return>", Output)

# Textbox
# textbox =tk.Text(root, height=1, font=('Roboto Mono Light', 16))
# textbox.pack(side='bottom', padx=[10, 100], pady=10)
# textbox.bind("<Return>", Output)
# Send button for text box
# sendbtn = ttk.Button(root, text='Send', command=Send)
# sendbtn.place(x=710, y=458, height=32)

# Send and Exit buttons
# btn = ttk.Button(text='Send', command=Send)
# btn.place(relx=0.88, rely=0.85) # btn.pack(expand=True, anchor=SE, padx=10)
# btn = ttk.Button(text='Exit', command=Exit)
# btn.place(relx=0.88, rely=0.90) # btn.pack(anchor=SE, padx=10, pady=[0, 10])

root.mainloop()