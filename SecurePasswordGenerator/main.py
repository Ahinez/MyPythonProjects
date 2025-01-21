import tkinter as tk
from tkinter import IntVar, StringVar, ttk
import random as r
import re

def set_elements():
    global chars
    chars = ''
    if digits_enabled.get() == 1: chars += digits
    if uppercase_letters_enabled.get() == 1: chars += uppercase_letters
    if lowercase_letters_enabled.get() == 1: chars += lowercase_letters
    if punctuation_checkbutton_enabled.get() == 1: chars += punctuation
    if ambiguous_characters_checkbutton_enabled.get() == 1:
        if 'l' in chars:
            chars = chars[:chars.find('l')] + chars[chars.find('l') + 1:]
            chars = chars[:chars.find('o')] + chars[chars.find('o') + 1:]
            chars = chars[:chars.find('i')] + chars[chars.find('i') + 1:]
        if '1' in chars:
            chars = chars[:chars.find('1')] + chars[chars.find('1') + 1:]
            chars = chars[:chars.find('0')] + chars[chars.find('0') + 1:]
        if 'L' in chars:
            chars = chars[:chars.find('L')] + chars[chars.find('L') + 1:]
            chars = chars[:chars.find('O')] + chars[chars.find('O') + 1:] 

def generate_password():
    global password
    password = ''
    for el in range(int(entry_len.get())):
        password += r.choice(chars)
    password_output['text'] = f'Password: {password}'

digits = "0123456789"
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
length = 0
cnt = 0

root = tk.Tk()
root.title('SPG')
root.geometry('500x500+700+300')
root.iconphoto(False, tk.PhotoImage(file = 'E:\Projects\MyPyhtonProjects\SecurePasswordGenerator\icons\key32.png'))

text1 = ttk.Label(text='Enter the number of passwords')
text2 = ttk.Label(text='Enter the password length')
text3 = ttk.Label(text='Password must contain: ')

chars = StringVar()

pass_cnt = ttk.Entry()

entry_len = ttk.Entry()
entry_len.grid(row=1, column=1, sticky='w')

digits_enabled = IntVar()
digit_checkbutton = ttk.Checkbutton(text='0123456789', variable=digits_enabled, command=set_elements)
digit_checkbutton.grid(row='3', column='0', sticky='w')

uppercase_letters_enabled = IntVar()
uppercase_letters_checkbutton = ttk.Checkbutton(text='ABCDEFEFGHIJKLMNOPQRSTUVWXYZ', variable=uppercase_letters_enabled, command=set_elements)
uppercase_letters_checkbutton.grid(row='4', column='0', sticky='w')

lowercase_letters_enabled = IntVar()
lowercase_letters_checkbutton = ttk.Checkbutton(text='abcdefghijklmnopqrstuvwxyz', variable=lowercase_letters_enabled, command=set_elements)
lowercase_letters_checkbutton.grid(row='5', column='0', sticky='w')

punctuation_checkbutton_enabled = IntVar()
punctuation_checkbutton = ttk.Checkbutton(text='!#$%&*+-=?@^_', variable=punctuation_checkbutton_enabled, command=set_elements)
punctuation_checkbutton.grid(row='6', column='0', sticky='w')

ambiguous_characters_checkbutton_enabled = IntVar()
ambiguous_characters_checkbutton = ttk.Checkbutton(text='Exclude ambiguous characters? (il1Lo0O)', variable=ambiguous_characters_checkbutton_enabled, command=set_elements)
ambiguous_characters_checkbutton.grid(row='7', column='0', sticky='w')

generate_btn = ttk.Button(text='Generate', command=generate_password)
generate_btn.bind()
generate_btn.grid(row=8, column=0)

password_output = ttk.Label()
password_output.grid(row=9, column=0, sticky='w')

text1.grid(row=0, column=0, sticky='w')
text2.grid(row=1, column=0, sticky='w')
pass_cnt.grid(row=0, column=1, sticky='w')
text3.grid(row=2, column=0, sticky='w')




root.mainloop()