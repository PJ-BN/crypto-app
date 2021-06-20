from tkinter import *

import tkinter.font as font

from bitcoin import Bitcoin
from binance import Binance
from cardano import Cardano
from dogecoin import Dogecoin
from ethereum import Ethereum
from tether import Tether


   
   
class Create:
    
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.grid(row=1,column=1)
        
        self.create()
    
    
    def create(self):
    
        myFont = font.Font(size=13)
        
        def destroyer():
            tit.destroy()
            bitcoin.destroy()
            ethereum.destroy()
            tether.destroy()
            dogecoin.destroy()
            bitcoin.destroy()
            cardano.destroy()
            binance.destroy()

        tit = Label(text="Crypto", font=font.Font(size=30))
        tit.grid(row=2, column=8, pady = 60)   
        
        def bcoin():
            destroyer()
            
            price = bitc.current()
            
            tit = Label(text="Bitcoin", font=font.Font(size=30))
            tit.grid(row=2, column=1, pady = 80)
            
            current = Label(text="Current ", font=myFont)
            current.grid(row=3, column=0)
            
            current_value = Label(text=f"$ {price}", font=myFont)
            current_value.grid(row=3, column= 1)
            
            calculate = Button(text="Calculate", font=myFont, bg="gray")
            calculate.grid(row=4, column= 0, pady = 80)
            
            y_price = bitc.yesterday()
            y_diff = bitc.y_diff
            y_per = bitc.y_per
            
            w_price = bitc.last_week()
            w_diff = bitc.w_diff
            w_per = bitc.w_per
            
            m_price = bitc.last_month()
            m_diff = bitc.m_diff
            m_per = bitc.m_per
            
            lst[1] = ("Price",f"{y_price}",f"{w_price}",f"{m_price}")
            lst[2] = ("Difference",f"{y_diff}",f"{w_diff}",f"{m_diff}")
            lst[3] = ("Diff Percentage",f"{y_per}",f"{w_per}",f"{m_per}")
            table = Table(window)
            
            
            

        bitcoin = Button(text="Bitcoin", bg="grey", height=3, width=17 , font=myFont, command=bcoin)
        bitcoin.grid(row=4, column=4, pady = 50, padx=25)
        
        
        def ecoin():
            destroyer()
            
            price = ethc.current()
            
            tit = Label(text="Ethereum", font=font.Font(size=30))
            tit.grid(row=2, column=1, pady = 80)
            
            current = Label(text="Current ", font=myFont)
            current.grid(row=3, column=0)
            
            current_value = Label(text=f"$ {price}", font=myFont)
            current_value.grid(row=3, column= 1)
            
            calculate = Button(text="Calculate", font=myFont, bg="gray")
            calculate.grid(row=4, column= 0, pady = 80)
            
            y_price = ethc.yesterday()
            y_diff = ethc.y_diff
            y_per = ethc.y_per
            
            w_price = ethc.last_week()
            w_diff = ethc.w_diff
            w_per = ethc.w_per
            
            m_price = ethc.last_month()
            m_diff = ethc.m_diff
            m_per = ethc.m_per
            
            lst[1] = ("Price",f"{y_price}",f"{w_price}",f"{m_price}")
            lst[2] = ("Difference",f"{y_diff}",f"{w_diff}",f"{m_diff}")
            lst[3] = ("Diff Percentage",f"{y_per}",f"{w_per}",f"{m_per}")
            table = Table(window)
            

        ethereum = Button(text="Ethereum", bg="grey", height=3, width=17, font=myFont, command=ecoin)
        ethereum.grid(row=4, column=8, pady = 50, padx=25)
        
        
        def tcoin():
            destroyer()
            
            price = tetc.current()
            
            tit = Label(text="Tether", font=font.Font(size=30))
            tit.grid(row=2, column=1, pady = 80)
            
            current = Label(text="Current ", font=myFont)
            current.grid(row=3, column=0)
            
            current_value = Label(text=f"$ {price}", font=myFont)
            current_value.grid(row=3, column= 1)
            
            calculate = Button(text="Calculate", font=myFont, bg="gray")
            calculate.grid(row=4, column= 0, pady = 80)
            
            y_price = tetc.yesterday()
            y_diff = tetc.y_diff
            y_per = tetc.y_per
            
            w_price = tetc.last_week()
            w_diff = tetc.w_diff
            w_per = tetc.w_per
            
            m_price = tetc.last_month()
            m_diff = tetc.m_diff
            m_per = tetc.m_per
            
            lst[1] = ("Price",f"{y_price}",f"{w_price}",f"{m_price}")
            lst[2] = ("Difference",f"{y_diff}",f"{w_diff}",f"{m_diff}")
            lst[3] = ("Diff Percentage",f"{y_per}",f"{w_per}",f"{m_per}")
            table = Table(window)
            

        tether = Button(text="Tether", bg="grey", height=3, width=17, font=myFont, command=tcoin)
        tether.grid(row=4, column=12, pady = 50, padx=25)
        
        
        def bicoin():
            destroyer()
            
            price = binc.current()
            
            tit = Label(text="Binance", font=font.Font(size=30))
            tit.grid(row=2, column=1, pady = 80)
            
            current = Label(text="Current ", font=myFont)
            current.grid(row=3, column=0)
            
            current_value = Label(text=f"$ {price}", font=myFont)
            current_value.grid(row=3, column= 1)
            
            calculate = Button(text="Calculate", font=myFont, bg="gray")
            calculate.grid(row=4, column= 0, pady = 80)
            
            y_price = binc.yesterday()
            y_diff = binc.y_diff
            y_per = binc.y_per
            
            w_price = binc.last_week()
            w_diff = binc.w_diff
            w_per = binc.w_per
            
            m_price = binc.last_month()
            m_diff = binc.m_diff
            m_per = binc.m_per
            
            lst[1] = ("Price",f"{y_price}",f"{w_price}",f"{m_price}")
            lst[2] = ("Difference",f"{y_diff}",f"{w_diff}",f"{m_diff}")
            lst[3] = ("Diff Percentage",f"{y_per}",f"{w_per}",f"{m_per}")
            table = Table(window)
            
            

        binance = Button(text="Binance", bg="grey", height=3, width=17, font=myFont, command=bicoin)
        binance.grid(row=10, column=4, pady = 50, padx=25)
        
        
        def carcoin():
            destroyer()
            
            price = carc.current()
            
            tit = Label(text="Cardano", font=font.Font(size=30))
            tit.grid(row=2, column=1, pady = 80)
            
            current = Label(text="Current ", font=myFont)
            current.grid(row=3, column=0)
            
            current_value = Label(text=f"$ {price}", font=myFont)
            current_value.grid(row=3, column= 1)
            
            calculate = Button(text="Calculate", font=myFont, bg="gray")
            calculate.grid(row=4, column= 0, pady = 80)
            
            y_price = carc.yesterday()
            y_diff = carc.y_diff
            y_per = carc.y_per
            
            w_price = carc.last_week()
            w_diff = carc.w_diff
            w_per = carc.w_per
            
            m_price = carc.last_month()
            m_diff = carc.m_diff
            m_per = carc.m_per
            
            lst[1] = ("Price",f"{y_price}",f"{w_price}",f"{m_price}")
            lst[2] = ("Difference",f"{y_diff}",f"{w_diff}",f"{m_diff}")
            lst[3] = ("Diff Percentage",f"{y_per}",f"{w_per}",f"{m_per}")
            table = Table(window)
            
            

        cardano = Button(text="Cardano", bg="grey", height=3, width=17, font=myFont, command=carcoin)
        cardano.grid(row=10, column=8, pady = 50, padx=25)
        
        
        def dogcoin():
            destroyer()
            
            price = dogc.current()
            
            tit = Label(text="Dogecoin", font=font.Font(size=30))
            tit.grid(row=2, column=1, pady = 80)
            
            current = Label(text="Current ", font=myFont)
            current.grid(row=3, column=0)
            
            current_value = Label(text=f"$ {price}", font=myFont)
            current_value.grid(row=3, column= 1)
            
            calculate = Button(text="Calculate", font=myFont, bg="gray")
            calculate.grid(row=4, column= 0, pady = 80)
            
            y_price = dogc.yesterday()
            y_diff = dogc.y_diff
            y_per = dogc.y_per
            
            w_price = dogc.last_week()
            w_diff = dogc.w_diff
            w_per = dogc.w_per
            
            m_price = dogc.last_month()
            m_diff = dogc.m_diff
            m_per = dogc.m_per
            
            lst[1] = ("Price",f"{y_price}",f"{w_price}",f"{m_price}")
            lst[2] = ("Difference",f"{y_diff}",f"{w_diff}",f"{m_diff}")
            lst[3] = ("Diff Percentage",f"{y_per}",f"{w_per}",f"{m_per}")
            table = Table(window)
            
            

        dogecoin = Button(text="Dogecoin", bg="grey", height=3, width=17, font=myFont, command=dogcoin)
        dogecoin.grid(row=10, column=12, pady = 50, padx=25)
        
        
class Table:
      
    def __init__(self,root):
          
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = Entry(root, width=17, bg="grey",
                               font=('Arial',15,'bold'))
                  
                self.e.grid(row=i+10, column=j)
                self.e.insert(END, lst[i][j])
  




bitc = Bitcoin()
binc = Binance()
carc = Cardano()
dogc = Dogecoin()
ethc = Ethereum()
tetc = Tether()


y_price = 0
y_diff = 0

lst = [("N/A", "Yesterday" , "Last Week", "Last Month"),
       ("Price",f"{y_price}",f"{y_price}",f"{y_price}"),
       ("Difference",f"{y_diff}",f"{y_diff}",f"{y_diff}"),
       ("Diff Percentage",f"{y_diff}",f"{y_diff}",f"{y_diff}")
       ]
        

total_rows = len(lst)
total_columns = len(lst[0]) 


window = Tk(className="Crypto Currencies")
window.geometry("800x600")


app = Create(window)

window.mainloop()

