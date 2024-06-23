from tkinter import *
exp=""
w=Tk()
def click(n):
    global exp
    exp=exp+str(n)
    v.set(exp)
def result():
    global exp
    result=eval(exp)
    v.set(result)
def clear():
    global exp
    exp=""
    v.set(exp)
v=StringVar()
#Step1 ->Design all the elements 1st
e=Entry(w,bg='cyan',font=("arial",20,'bold'),textvariable=v)
b1=Button(w,text="1",font=("arial",15,'bold'),command=lambda:click(1))
b2=Button(w,text="2",font=("arial",15,'bold'),command=lambda:click(2))
b3=Button(w,text="3",font=("arial",15,'bold'),command=lambda:click(3))
b4=Button(w,text="4",font=("arial",15,'bold'),command=lambda:click(4))
b5=Button(w,text="5",font=("arial",15,'bold'),command=lambda:click(5))
b6=Button(w,text="6",font=("arial",15,'bold'),command=lambda:click(6))
b7=Button(w,text="7",font=("arial",15,'bold'),command=lambda:click(7))
b8=Button(w,text="8",font=("arial",15,'bold'),command=lambda:click(8))
b9=Button(w,text="9",font=("arial",15,'bold'),command=lambda:click(9))
b0=Button(w,text="0",font=("arial",15,'bold'),command=lambda:click(0))
b10=Button(w,text="=",font=("arial",15,'bold'),command=lambda:result())
b11=Button(w,text="clear",font=("arial",15,'bold'),command=lambda:clear())
b12=Button(w,text="+",font=("arial",15,'bold'),command=lambda:click('+'))
b13=Button(w,text="-",font=("arial",15,'bold'),command=lambda:click('-'))
b14=Button(w,text="*",font=("arial",15,'bold'),command=lambda:click('*'))
b15=Button(w,text="/",font=("arial",15,'bold'),command=lambda:click('/'))
#step2 Place all the component in good place we are using grid() methode
e.grid(row=1,column=1,columnspan=4)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)
b3.grid(row=2,column=3)
b4.grid(row=2,column=4)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=3,column=3)
b8.grid(row=3,column=4)
b9.grid(row=4,column=1)
b0.grid(row=4,column=2)
b10.grid(row=4,column=3)
b11.grid(row=4,column=4)
b12.grid(row=5,column=1)
b13.grid(row=5,column=2)
b14.grid(row=5,column=3)
b15.grid(row=5,column=4)
w.mainloop()
