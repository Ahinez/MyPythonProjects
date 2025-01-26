import tkinter as tk
from tkinter import ttk
import random as r

def toggle_advanced_settings():
    if checkbtn_var.get():
        def check_input(event):
            global chars
            global length
            length = 0
            try:
                length = int(entry_len.get())
                if length > 0 and chars != '':
                    generate_btn.config(state=tk.ACTIVE)
                else:
                    generate_btn.config(state=tk.DISABLED)
            except ValueError:
                generate_btn.config(state=tk.DISABLED)

        def set_elements():
            global chars
            global length
            chars = ''
            if digits_enabled.get():chars += digits
            if uppercase_letters_enabled.get(): chars += uppercase_letters
            if lowercase_letters_enabled.get() == 1: chars += lowercase_letters
            if punctuation_checkbutton_enabled.get(): chars += punctuation
            if ambiguous_characters_checkbutton_enabled.get():
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
            if chars == '' or length == 0:
                generate_btn.config(state=tk.DISABLED)
            else:
                generate_btn.config(state=tk.ACTIVE)

        def generate_password():
            global password
            password = ''
            for el in range(int(entry_len.get())):
                password += r.choice(chars)
            password_output.grid(row=9, column=0, sticky='w')
            password_output['text'] = f'Password: {password}'
            copy_btn = ttk.Button(text='Copy', command=clipboard)
            copy_btn.grid(row=9, column=1)

        def clipboard():
            global password
            new_window.clipboard_clear()
            new_window.clipboard_append(password)
            password_output['text'] = 'Password copied to clipboard'

        digits = "0123456789"
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        punctuation = '!#$%&*+-=?@^'

        new_window = tk.Toplevel(root)
        new_window.title('SPG')
        new_window.geometry('+700+350')
        new_window.iconphoto(False, tk.PhotoImage(file = 'E:\Projects\MyPyhtonProjects\SecurePasswordGenerator\icons\key32.png'))

        text2 = ttk.Label(new_window, text='Enter the password length')
        text3 = ttk.Label(new_window, text='Password must contain: ')

        chars = ''

        entry_len = ttk.Entry(new_window)
        length = 0
        entry_len.bind("<KeyRelease>", check_input)
        entry_len.grid(row=1, column=1, sticky='w')

        digits_enabled = tk.BooleanVar(value=False)
        digit_checkbutton = ttk.Checkbutton(new_window, text='0123456789', variable=digits_enabled, command=set_elements)
        digit_checkbutton.grid(row='3', column='0', sticky='w')

        uppercase_letters_enabled = tk.BooleanVar(value=False)
        uppercase_letters_checkbutton = ttk.Checkbutton(new_window, text='ABCDEFEFGHIJKLMNOPQRSTUVWXYZ', variable=uppercase_letters_enabled, command=set_elements)
        uppercase_letters_checkbutton.grid(row='4', column='0', sticky='w')

        lowercase_letters_enabled = tk.BooleanVar(value=False)
        lowercase_letters_checkbutton = ttk.Checkbutton(new_window, text='abcdefghijklmnopqrstuvwxyz', variable=lowercase_letters_enabled, command=set_elements)
        lowercase_letters_checkbutton.grid(row='5', column='0', sticky='w')

        punctuation_checkbutton_enabled = tk.BooleanVar(value=False)
        punctuation_checkbutton = ttk.Checkbutton(new_window, text='!#$%&*+-=?@^_', variable=punctuation_checkbutton_enabled, command=set_elements)
        punctuation_checkbutton.grid(row='6', column='0', sticky='w')

        ambiguous_characters_checkbutton_enabled = tk.BooleanVar(value=False)
        ambiguous_characters_checkbutton = ttk.Checkbutton(new_window, text='Exclude ambiguous characters? (il1Lo0O)', variable=ambiguous_characters_checkbutton_enabled, command=set_elements)
        ambiguous_characters_checkbutton.grid(row='7', column='0', sticky='w')

        generate_btn = ttk.Button(new_window, text='Generate', state=tk.DISABLED, command=generate_password)
        generate_btn.bind()
        generate_btn.grid(row=8, column=0)

        entry = tk.Entry(new_window)
        entry.config(state="readonly")

        password_output = ttk.Label(new_window)

        text2.grid(row=1, column=0, sticky='w')
        text3.grid(row=2, column=0)
    else:
        for window in root.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()

root = tk.Tk()

root.title('SPG')
root.geometry('+700+300')
root.iconphoto(False, tk.PhotoImage(file = 'E:\Projects\MyPyhtonProjects\SecurePasswordGenerator\icons\key32.png'))

checkbtn_var = tk.BooleanVar()

advanced_settings_checkbtn = tk.Checkbutton(root, text='Advansed Settings', variable=checkbtn_var, command=toggle_advanced_settings)
advanced_settings_checkbtn.grid()

root.mainloop()