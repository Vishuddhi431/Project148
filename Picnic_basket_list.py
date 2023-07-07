#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 08:18:33 2023

@author: vishuddhimakeshwaran
"""

from tkinter import * 
import random

root = Tk()
root.title("Picnic Basket List")
root.geometry("400x500")

list1 = ["blanket", "basket", "sandwiches", "snacks", "frisbee", "water", "cutlery", "napkins"]

labelList = Label(root)
labelList["text"] = "List of items: " + str(list1)
labelList.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label1 = Label(root)

def gen(): 
    randomNo = random.randint(0, len(list1) - 1)
    label1["text"] = "Pack " + list1[randomNo] + " into the bag"
    #Try sample range thing
    
button1 = Button(root, text = "What item to pack", command = gen)
button1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.6, anchor = CENTER)
root.mainloop()