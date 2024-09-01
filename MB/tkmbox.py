import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My Form")
root.geometry("400x300+200+150")


label1 = tk.Label(root, text="نام")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()


def button1_click():
    messagebox.showinfo(title="MB", message=f"Hello {entry1.get()}!")
    

button1 = tk.Button(root, text="ثبت", command=button1_click)
button1.pack()

root.mainloop()