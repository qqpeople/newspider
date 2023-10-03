from tkinter import *

root = Tk()
root.title("sbsbsb")
root.geometry('400x400')

var = StringVar()
l = Label(root,textvariable=var,font=100,width=10,height=5)
l.pack()

zhiti = Label(root,text="成林是sb",font=100,width=10,height=5)
zhiti.pack()

yes = Button(root,text="同意",bg="red",width=10,height=3)
yes.pack()

root.mainloop()

