#from tkinter import Label, Button, END
from tkinter.tix import Tk, Control, ComboBox
from tkinter.tix import *
import tkinter.tix

top = Tk()
#top.tk.eval('package require Tix')
lb = Label(top, text='Fruits (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Control(top, label='Number:', integer=True, max=12, min=2, value=2, step=2)
ct.label.config(font='Helvetica -14 bold')
ct.pack()

cb = ComboBox(top, label='Type:', editable=True)
for fruites in ('Apple', 'Orange', 'Mango', 'Papaya'):
    cb.insert(END, fruites)
cb.pack()

qb = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()

