# https://iconscout.com/icons/ico
# https://medium.com/@asusrishabh/convert-python-program-to-exe-c773345716df
# https://www.javatpoint.com/python-tkinter

import tkinter as tk

screen = tk.Tk()

screen.geometry('400x400')

screen.title('Create file')

screen.iconbitmap('logo.ico')

def create_file():
    import os
    path_ = path.get()
    name_ = name.get()
    filename = os.path.join(path_, name_)

    file = open(filename, 'x')
    if file:
        tk.Label(screen, text=f"file is created : {name_}").grid(row=3, column=1)

    print(path_, name_)


tk.Label(screen, text="Enter Path: ").grid(row=0, column=0)
path = tk.Entry(screen)
path.grid(row=0, column=1)
tk.Label(screen, text="Enter filename: ").grid(row=1, column=0)
name = tk.Entry(screen)
name.grid(row=1, column=1)

tk.Button(screen, text="Save", fg="red", bg="black", command=create_file).grid(row=2, column= 1)
screen.mainloop()