import tkinter as tk
from tkinter import ttk
from random import choice

def Send():
    output['text'] = f'Your question is: {entry.get()}\nAnswer: {choice(answers)}'

def Output(event):
    output['text'] = f'Your question is: {entry.get()}\nAnswer: {choice(answers)}'

answers = ['Undeniably', 'Foregone', 'There\'s no doubt about it', 'Definitely yes', 'You can be sure of that', 'I think so', 'Most likely', 'Good prospects', \
           'The signs say yes', 'Yes', 'It\'s not clear yet, try again', 'Ask me later', 'It\'s better not to tell', 'There\'s no way to predict right now', 'Concentrate and ask again', \
            'Don\'t even think about it', 'My answer is no', 'Not according to my records', 'The outlook is not good', 'It\'s highly doubtful']

root = tk.Tk()

root.title('8Ball')

root.iconbitmap('E:\Projects\MyPyhtonProjects\8Ball (Tkinter)\8ball.ico')

root.geometry('800x500+600+300')
root.resizable(False, False)

label = tk.Label(text="Ask your question", font=('Roboto Mono Light', 18))
label.pack(padx=20, pady=20)

output = tk.Label(relief='groove', font=('Roboto Mono Light', 14))
output.pack(expand=1, padx=10, fill='both')

entry = ttk.Entry()
entry.pack(side='bottom', pady=10, fill='x', padx=[10,95])
entry.bind("<Return>", Output)

btn = ttk.Button(text='Send', command=Send)
btn.place(relx=0.89, rely=0.94)

root.mainloop()