import tkinter.ttk
from tkinter import Button, END, Label, W
from tkinter import *
import Pmw
#from Pmw import initialise, ComboBox, Counter
from pmw import *
from tkinter.tix import *

top = Tk()
Pmw.initialise(top)

lb = Label(top,text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Pmw.Counter(top, labelpos=W, label_text='Number:', datatype='integer', entryfield_value=2, increment=2, entryfield_validate={'validator':'integer', 'min': 2, 'max': 12})
ct.pack()

cb = Pmw.ComboBox(top, labelpos=W, label_text='Type:')
for animal in ('dog', 'cat', 'hamster', 'python'):
 cb.insert(END, animal)
cb.pack()

qb = Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
qb.pack()

top.mainloop()

