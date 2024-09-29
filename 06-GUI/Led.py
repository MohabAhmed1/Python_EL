from tkinter import *

root = Tk()
root.geometry('400x400')

canvas = Canvas(root, width=400, height=250,bg='lightblue')
canvas.pack(side=TOP)

btn_frame = Frame(root)
btn_frame.pack(pady=10)

cx, cy = 200, 125  # Center of the circle
r = 50             # Radius of the circle

canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='blue', fill='grey', width=3)
lbl = Label(btn_frame, text='')
lbl.pack()

def Led_ON():
    global cx,cy,r
    lbl.config(text='')
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='blue', fill='yellow', width=3)
    lbl.config(text='LED is ON')

def Led_OFF():
    global cx,cy,r
    lbl.config(text='')
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline='blue', fill='grey', width=3)  
    lbl.config(text='LED is OFF')

led_on = Button(btn_frame,text='Led ON',command=Led_ON)
led_off = Button(btn_frame,text='Led OFF',command=Led_OFF)

led_on.pack(pady=10)
led_off.pack()

root.mainloop()
