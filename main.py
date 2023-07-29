import customtkinter as ctk
import os


def write_in_box(val):
    listbox.configure(state="normal")
    entry_nr = int(float(listbox.index('end'))) - 1
    listbox.insert(index=ctk.END, text=str(entry_nr) + '. ' + val.capitalize() + '\n')
    listbox.configure(state="disabled")


def get_entry():
    val = entry.get()
    with open('data.txt', 'w') as file1:
        file1.write(str(int(float(listbox.index('end'))) - 1) + '. ' + val.capitalize() + '\n')
        # file1.write(listbox.get(1.0, ctk.END))
    write_in_box(val)
    entry.delete(0, len(val))


def del_entry():
    listbox.configure(state="normal")


root = ctk.CTk()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

ctk.set_default_color_theme("dark-blue")
root.geometry("420x420")
root.resizable(width=False, height=False)
root.title("To Do List")

lbl = ctk.CTkLabel(root, text='Things to do', font=('Century Gothic', 30)).grid(row=0, column=0,
                                                                                sticky='w', padx=15)
listbox = ctk.CTkTextbox(root, width=300, height=290, state="disabled", font=('Century Gothic', 15),
                         fg_color='#242424', activate_scrollbars=False, border_spacing=1, border_width=1,
                         border_color='black')
listbox.grid(column=0, row=1, columnspan=2, sticky='w', padx=15)


entry = ctk.CTkEntry(root, width=300, font=('Century Gothic', 30), placeholder_text='Enter task here')
entry.grid(column=0, row=2, sticky='w', padx=15)

btn = ctk.CTkButton(root, text="Submit", width=60, height=40, command=get_entry)\
    .grid(column=1, row=2, sticky='w')

btn_del = ctk.CTkButton(root, text="Modify", width=60, height=40, command=del_entry)\
    .grid(column=1, row=1, sticky='nw', pady=10)

if os.path.getsize('data.txt') > 0:
    listbox.configure(state="normal")
    entry_num = int(float(listbox.index('end'))) - 1
    with open('data.txt', 'r') as file:
        text = file.read()
        listbox.insert(index=ctk.END, text=text + '\n')
        listbox.configure(state="disabled")

root.mainloop()


