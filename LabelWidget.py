from tkinter import *
myroot = Tk()
myroot.resizable(width=True,height=True)

labelWidget = Label(myroot,text='Label1',bd=8,relief='groove')
labelWidget.pack()

myroot.mainloop()