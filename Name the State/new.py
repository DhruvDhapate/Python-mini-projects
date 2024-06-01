from tkinter import *
from tkinter import Tk

window = Tk()
window.title("Miles to Km Conversion")
window.config(padx=50, pady=50)


def convert():
    miles = int(entry.get())
    ans = miles * 1.6
    label_3.config(text=ans)


entry = Entry(width=10)
entry.grid(row=0, column=1)

label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="Km")
label_4.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
