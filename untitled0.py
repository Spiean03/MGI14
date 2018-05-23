# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:38:10 2016

@author: Administrator
"""
import os
import Tkinter as Tk

root = Tk.Tk()
logo = Tk.PhotoImage(file= os.getcwd()+"\Map_of_the_sample_1.jpg")
w1 = Tk.Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w2 = Tk.Label(root, 
           justify=Tk.LEFT,
           padx = 10, 
           text=explanation).pack(side="left")
root.mainloop()