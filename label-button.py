from tkinter import *

top = Tk()
top.geometry('250x150')
label = Label(top, text='Welcome to MCE', font = 'Arial 16 bold',bg='gold', fg='white')
label.pack()



scale = Scale(top, from_=1, to=8,orient=HORIZONTAL,bg='white', fg='black')
#scale.set(12)
scale.pack(fill=Y, expand=1)

quit = Button(top, text='Submit', command=top.quit,bg='blue', fg='yellow')
quit.pack()

top.mainloop()