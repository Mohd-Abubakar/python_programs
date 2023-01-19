from tkinter import *
from tkinter.messagebox import *

root = Tk()
#root.geometry("500x400")




e = lambda: showerror('Error', 'Error Button Pressed!')
w = lambda: showwarning('Error', 'warning Button Pressed!')
i = lambda: showinfo('Error', 'Info Button Pressed!')

a = Button(root, bg="red", text="error", command=e)
a.pack(fill =X )

a = Button(root, bg="yellow", text="warning", command=w)
a.pack( fill =X )

a = Button(root, bg="blue", fg='white', text="info", command=i)
a.pack(fill =X)

q= Button(root, text="QUIT", command=root.quit)
q.pack()
root.mainloop()
