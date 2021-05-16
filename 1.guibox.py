from tkinter import *
root = Tk()

root.title('My Box Gui')
root.iconbitmap('apple.ico')
root.geometry("500x300")

my_label1 = Label(root, text="Hello World ").pack()
my_label2 = Label(root, text="I love Pyhton !!").pack()


root.mainloop()
