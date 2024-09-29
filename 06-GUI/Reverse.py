from tkinter import *


root = Tk()
entries = Frame(root)
entries.pack()
word = StringVar()
root.geometry('300x150')

def Rev():
    global word
    reversed_word = word.get()[::-1]  
    Label(root,text='The reversed Word').pack(side=BOTTOM)
    lbl_wrd = Label(root,text=reversed_word).pack(side=BOTTOM)


lbl = Label(entries,text='Enter a Word :').pack(side=LEFT)
Entre = Entry(entries,textvariable = word ).pack(side=RIGHT)
btn = Button(root,text='Validate' , command=Rev ).pack(side=BOTTOM)

root.mainloop()