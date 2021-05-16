from tkinter import *
root = Tk()

root.title("Radio Button")
root.iconbitmap('apple.ico')
root.geometry("800x800")


q = IntVar()

q.get()
q.set('2')  # it sets by default the value as 2


def clickme(value):
    label = Label(root, text=value)
    label.pack()


Radiobutton(root, text="Option 1", variable=q, value=1).pack(anchor='w')
Radiobutton(root, text="Option 2", variable=q, value=2).pack(anchor='w')
Radiobutton(root, text="Option 3", variable=q, value=3).pack(anchor='w')
Radiobutton(root, text="Option 4", variable=q, value=4).pack(anchor='w')

label = Label(root, text=q.get())
label.pack()

b = Button(root, text="SUBMIT", command=lambda: clickme(q.get()))
b.pack()

root.mainloop()
