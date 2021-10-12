from tkinter import *
from tkinter import ttk
from numpy import binary_repr
Root=Tk()
def getresult():
    try:
        value=int(decim_value.get())
        print(binary_repr(value,None))
        Binary_value.set(binary_repr(value,None))
    except:
        pass
decim_value=StringVar()
Binary_value=StringVar()
label_decim=Label(text="decimal value")
decimal_value=Entry(textvariable=decim_value)
label_binary=Label(text="the binary value is")
label_result=Label(textvariable=Binary_value)
btn=Button(text="calculate",command=getresult)
label_decim.grid(row=0,column=0)
decimal_value.grid(row=0,column=1)
label_binary.grid(row=1,column=0)
label_result.grid(row=1,column=1,sticky=(W , E))
btn.grid(row=2,column=0)
Root.mainloop()
