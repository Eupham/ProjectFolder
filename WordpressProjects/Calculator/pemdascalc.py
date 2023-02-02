import tkinter as tk

def append_to_display(v):
    display.set(display.get() + v)

def button_clear():
    display.set("")

def button_add():
    first_number = display.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "addition"
    display.set("")

def button_equal():
    second_number = display.get()
    display.set(f_num + int(second_number))

root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

display = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display, width=20, font=("Helvetica", 16))
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [tk.Button(root, text=str(i), padx=40, pady=20, command=lambda x=i: append_to_display(str(x))) for i in range(10)]

for i, button in enumerate(buttons):
    button.grid(row=1 + i // 3, column=i % 3)

button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_add.grid(row=4, column=0)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=3)

for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

root.mainloop()