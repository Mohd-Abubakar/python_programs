from functools import partial as pto
from tkinter import Tk, Button, X
#from tkMessageBox import showinfo, showwarning, showerror
from tkinter.messagebox import *

#WARN = 'warn'
#CRIT = 'crit'
#REGU = 'regu'

SIGNS = {
    'do not enter': 'CRIT',
    'railroad crossing': 'WARN',
    '55\nspeed limit': 'REGU',
    'wrong way': 'CRIT',
    'merging traffic': 'WARN',
    'one way': 'REGU',
    }

critCB = lambda: showerror('Error', 'CRITICAL SIGNAL')
warnCB = lambda: showwarning('Warning', 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text='QUIT', command=top.quit, bg='red', fg='white').pack()


MyButton = pto(Button, top)
CritButton = pto(MyButton, command=critCB, bg='white', fg='red')
WarnButton = pto(MyButton, command=warnCB, bg='gold')
ReguButton = pto(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r).pack(fill=X, expand=True)' % (signType.title(),eachSign)

    #cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)'% (signType.title(), eachSign, '.title()')
    eval(cmd)

top.mainloop()

