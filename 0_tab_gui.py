import tkinter as tk                    
from tkinter import *
from tkinter import ttk
  
root = tk.Tk()
root.title("Tab")
root.geometry("200x150")
tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='JinBae')
tabControl.add(tab2, text ='MiBae')
tabControl.add(tab3, text ='ChunBae')
tabControl.add(tab4, text ='MuBae')
tabControl.pack(expand = 1, fill ="both")
  
# l1=tk.Label(tab1,text='I am JinBae',bg='yellow',width=10)
# l1.grid(row=1,column=1) # using grid 
photo_1 =PhotoImage(file="jinbae.png")
b1=tk.Button(tab1,text='I MiBae', image=photo_1)
b1.place(relx=0.4,rely=0) 

# l2=tk.Label(tab2,text='I am tab-1',bg='yellow',width=10)
# l2.grid(row=1,column=1) # using grid 
photo_2 =PhotoImage(file="Mibae.png")
b2=tk.Button(tab2,text='I am MiBae', image=photo_2)
b2.place(relx=0.4,rely=0) 

photo_3 =PhotoImage(file="chunbae_1.png")
b3=tk.Button(tab3,text='I am ChunBae', image=photo_3)
b3.place(relx=0.4,rely=0) 

photo_4 =PhotoImage(file="Mubae.png")
b4=tk.Button(tab4,text='I am MuBae', image=photo_4)
b4.place(relx=0.4,rely=0) 
  
root.mainloop()  
