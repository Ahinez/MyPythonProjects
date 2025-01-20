import tkinter as tk
from tkinter import IntVar, ttk
import random as r

def add_digits():
    global chars
    chars += digits

def add_uppercase_letters():
    global chars
    chars += uppercase_letters

def add_lowercase_letters():
    global chars
    chars += lowercase_letters

def add_punctuation():
    global chars
    chars += punctuation

def reduce_ambiguous_characters():
    global chars
    char = char[:char.find('i')] + char[char.find('i') + 1:]
    char = char[:char.find('l')] + char[char.find('l') + 1:]
    char = char[:char.find('1')] + char[char.find('1') + 1:]
    char = char[:char.find('L')] + char[char.find('L') + 1:]
    char = char[:char.find('o')] + char[char.find('o') + 1:]
    char = char[:char.find('0')] + char[char.find('0') + 1:]
    char = char[:char.find('O')] + char[char.find('0') + 1:]

def generate_password():
    global password
    for el in range(int(pass_len.get())):
        password += r.choice(chars)
    text4['text'] = f'Password: {password}'

digits = "0123456789"
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
chars = ''
password = ''
length = 0
cnt = 0

root = tk.Tk()
root.title('SPG')
root.geometry('500x500+700+300')
root.iconphoto(False, tk.PhotoImage(file = 'E:\Projects\MyPyhtonProjects\SecurePasswordGenerator\icons\key32.png'))

enabled = IntVar()
enabled2 = IntVar()
enabled3 = IntVar()
enabled4 = IntVar()
enabled5 = IntVar()

text1 = ttk.Label(text='Enter the number of passwords')
text2 = ttk.Label(text='Enter the password length')
text3 = ttk.Label(text='Password must contain: ')
text4 = ttk.Label(text='Password: ')


pass_cnt = ttk.Entry()

pass_len = ttk.Entry()

btn = ttk.Button(text='Generate', command=generate_password)


digit_checkbutton = ttk.Checkbutton(text='0123456789', variable=enabled, command=add_digits)
uppercase_letters_checkbutton = ttk.Checkbutton(text='ABCDEFEFGHIJKLMNOPQRSTUVWXYZ', variable=enabled2, command=add_uppercase_letters)
lowercase_letters_checkbutton = ttk.Checkbutton(text='abcdefghijklmnopqrstuvwxyz', variable=enabled3, command=add_lowercase_letters)
punctuation_checkbutton = ttk.Checkbutton(text='!#$%&*+-=?@^_', variable=enabled4, command=add_punctuation)
ambiguous_characters_checkbutton = ttk.Checkbutton(text='Exclude ambiguous characters? (il1Lo0O)', variable=enabled5, command=reduce_ambiguous_characters)


text1.grid(row=0, column=0, sticky='w')
text2.grid(row=1, column=0, sticky='w')
pass_cnt.grid(row=0, column=1, sticky='w')
pass_len.grid(row=1, column=1, sticky='w')
text3.grid(row=2, column=0, sticky='w')
digit_checkbutton.grid(row='3', column='0', sticky='w')
uppercase_letters_checkbutton.grid(row='4', column='0', sticky='w')
lowercase_letters_checkbutton.grid(row='5', column='0', sticky='w')
punctuation_checkbutton.grid(row='6', column='0', sticky='w')
ambiguous_characters_checkbutton.grid(row='7', column='0', sticky='w')
text4.grid(row=8, column=0, sticky='w')
btn.grid(row=9, column=0)


root.mainloop()