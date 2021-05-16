from tkinter import *
root = Tk()

root.title("Entry field")
root.iconbitmap('apple.ico')
root.geometry("800x800")

e = Entry(root, width=50, fg='red')
e.grid(row=0, column=1)

ee = Entry(root, width=50, fg='black')
ee.grid(row=0, column=2)


def clickme():
    mylabel = Label(root, text="Hello " + e.get())
    mylabel.grid(row=1, column=1)
    e.delete(0, END)  # deletes the input for the next iteration


def clickme2():
    mylabel = Label(root, text="Hello " + ee.get())
    mylabel.grid(row=1, column=2)
    ee.delete(0, END)  # deletes the input for the next iteration


b = Button(root, text="Enter your first name", padx=10, pady=10,
           bg='white', fg='green', command=clickme)
b.grid(row=3, column=1)
b = Button(root, text="Enter your last name", padx=10, pady=10,
           bg='white', fg='green', command=clickme2)
b.grid(row=3, column=2)

root.mainloop()
