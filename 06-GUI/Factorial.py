from tkinter import *


root = Tk()
entries = Frame(root)
entries.pack()
num = IntVar()
root.geometry('300x150')
lbl_result = Label(root,text='')
lbl_result.pack(pady=15)

def Factorial():
    global num
    result = 1
    number = num.get()
    
    lbl_result.config(text='')
    while(number!=0):
        result = number * result
        number = number - 1 
    lbl_result.config(text=f'The factorial of {num.get()}={result}').pack(pady=15)


lbl = Label(entries,text='Enter a value of integer :').pack(side=LEFT)
Entre = Entry(entries,textvariable = num ).pack(side=RIGHT)
btn = Button(root,text='Evaluate' , command=Factorial ).pack(pady=10)

root.mainloop()