from tkinter import *


root = Tk()
root.geometry('300x150')
entries = Frame(root)
entries.pack()
lbl = Label(root,text='')
lbl.pack()
M = IntVar()
N = IntVar()
sum_subtract = IntVar()
def Operation():
    global M,N,sum_subtract
    lbl.config(text='')
    if (sum_subtract.get() == 1):
        summ = M.get() + N.get()
        lbl.config(text=f'The Sum is {M.get()} + {N.get()} = {summ}')
    elif(sum_subtract.get() == 2):
        subtract = M.get() - N.get()
        lbl.config(text=f'The Subtraction is {M.get()} - {N.get()} = {subtract}')  

lbl_M = Label(entries,text='Enter the value of M:').grid(row=0,column=0)
lbl_N = Label(entries,text='Enter the value of N:').grid(row=1,column=0)
M_entry = Entry(entries,textvariable=M).grid(row=0,column=1)
N_entry = Entry(entries,textvariable=N).grid(row=1,column=1)

rad1 = Radiobutton(root,text='Sum',variable=sum_subtract,value=1).pack()
rad2 = Radiobutton(root,text='Subtract',variable=sum_subtract,value=2).pack()

btn = Button(root, text='Evaluate', command= Operation).pack()


root.mainloop()