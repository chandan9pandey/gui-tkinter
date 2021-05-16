from tkinter import *
root = Tk()

root.title("Gui Button")
root.iconbitmap('apple.ico')
root.geometry("500x500")


def myclick():
    mylabel = Label(root, text="WELCOME to the Course !", fg='#3371ff').pack()


mybutton = Button(root, text="Hey CLICK me !", fg='yellow',
                  bg='black', command=myclick, padx=30, pady=50)

mybutton.pack()

root.mainloop()
