from tkinter import *
root = Tk()

root.title("Learn Grid")
root.iconbitmap('apple.ico')
root.geometry("500x500")

my_label = Label(root, text="My new GUI app!")
my_label2 = Label(root, text="This is line 2")

my_label.grid(row=0, column=1)
my_label2.grid(row=0, column=2)

root.mainloop()
