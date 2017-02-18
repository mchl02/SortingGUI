from Tkinter import *
from math import *
AwesomeList = []


def evaluate(event):
    for x in eval(entry.get()):
         AwesomeList.append(x)
    
    root.configure(text=str(sorted(AwesomeList)))
    entry.delete(0,END)
    del AwesomeList[:]
def reset():
    del AwesomeList[:]
w = Tk()
Label(w, text="The numbers you want to sort:").pack()
entry = Entry(w)
label = Label(w)
entry.bind("<Return>", evaluate)
entry.pack()
root = Label(w)
root.pack()
w.mainloop()



