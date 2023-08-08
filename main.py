###### *** Create by Falcon Sumat *** ######
  
   # Currency Converter  #

#1. Enter Amount Here        :    5    :
#2. Enter Currency Name      :   USD   :
#3  Enter Required Currency  :   INR   :
  
          # :Click: #
          
     #      :₹ 410.132        #



from currency_converter import CurrencyConverter
from tkinter import Tk, ttk
from tkinter import *
import tkinter as tk

a = CurrencyConverter()

#colors 
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#EB5D51"  # red

window = tk.Tk()
window.geometry('500x400')
window.title('Converter')
window.configure(bg=cor0)
window.resizable(height = FALSE, width=FALSE)

def clicked():
    amount = int(e1.get())
    cur1 = e2.get()
    cur2 = e3.get()
    data = a.convert(amount,cur1, cur2)
    l5 = tk.Label(window, text=data, font="Times 25 bold").place(x = 120, y = 290)

l1 = tk.Label(window,text="Currency Converter", font="Times 25 bold").place(x = 100, y = 30)

l2 = tk.Label(window,text="Enter amount here", font="Times 15 bold").place(x = 50, y = 80)
e1 = tk.Entry(window)

l3 = tk.Label(window,text="Enter Currency", font="Times 15 bold").place(x = 50, y = 130)
e2 = tk.Entry(window)

l4 = tk.Label(window,text="Enter req Currency", font="Times 15 bold").place(x = 50, y = 180)
e3 = tk.Entry(window)

b1 = tk.Button(window, text="click", command=clicked).place(x = 230, y = 240)
e1.place(x = 300, y = 90)
e2.place(x = 300, y = 140)
e3.place(x = 300, y = 190)


window.mainloop()



     # Currency Converter  #

#1. Enter Amount Here        :    5    :
#2. Enter Currency Name      :   USD   :
#3  Enter Required Currency  :   INR   :
  
          # :Click: #
          
     #      :₹ 410.132        #











