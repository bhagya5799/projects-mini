
from cgitb import text
from tkinter import*
import tkinter as tk
import calendar
from turtle import width
root =tk.tk()
root.geometry("400x300")
root.title("calender")
def show():
    m=int(month.get())
    y=int(year.get())
    output=calendar.month(y,m)
    cal.inser("end",output)
def clear():
    cal.delate(1.0,"end")
def exit():
    root.destory()
m_label=Label(root,text="month,",font=("vardan","10","bold"))
m_label.place(x=70,y=80)
month=Spinbox(root,from_=1,to=12,width="5")
month.place(x=140,y=80)
y_label=Label(root,text="year",font=("verdana","10","b0ld"))
y_label.place(x=210,y=80)
year=Spinbox(root,from_=2020,to=3000,width="8")
year.place(x=260,y=80)
cal=text(root,width=33,height=8,_Relief=RIDGE,borderwidth=2)
cal.place(x=70,y=110)
show=Button(root,text="show",font=("verdana",10,"bold"),relief=RIDGE,borderwidth=2,command=show)
show.Place(x=140,y=250)
clear=Button(root,text="show",font=("verdana",10,"bold"),relief=RIDGE,borderwidth=2,command=clear)
clear.place(x=200,y=250)
exit=Button(root,text="exit",font=("verdana",10,"bold"),relief=RIDGE,borderwidth=2,command=exit)
exit.Place(x=260,y=250)
root.mainloop()



