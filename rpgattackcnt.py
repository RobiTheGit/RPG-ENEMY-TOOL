#!/usr/bin/python3
import random
from tkinter import *
import customtkinter
import tkinter as tk
import attackroll
import sys
from tktooltip import ToolTip
global output
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        global luck
        global mini
        global maxi
        global mods
        global lucktype
        global output
        global die
        global c2
        global toroll    
        photo = PhotoImage(file ="dieicon.png")
        root.iconphoto(False, photo)   
        lucktype = tk.IntVar()       
        mods = tk.IntVar()
        luck = tk.IntVar()
        mini = tk.IntVar()
        maxi = tk.IntVar()
        die = tk.IntVar()
        leftframe = customtkinter.CTkFrame(
        root
        )        
        leftframe.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        topframe = customtkinter.CTkFrame(
        root 
        )
        topframe.pack(side = TOP, fill=X, expand=1)
                
        bottomframe = customtkinter.CTkFrame(
        root 
        )
        bottomframe.pack(side = TOP, fill=BOTH, pady = 5, expand=1)
        l0 = customtkinter.CTkLabel(topframe, text="RPG Enemy Damage Tool", font = ('Z003', 20))
        l0.pack()
                               
        l1 = customtkinter.CTkLabel(leftframe, text="Die min and max (To hit)", font = ('Z003', 20))
        l1.pack()
        self.entrythingy = customtkinter.CTkEntry(leftframe, placeholder_text="1", font = ('Z003', 20))
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("1")
        self.entrythingy["textvariable"] = self.contents
        
        self.entrythingy2 = customtkinter.CTkEntry(leftframe, placeholder_text="20", font = ('Z003', 20))
        self.entrythingy2.pack()
        self.contents2 = tk.StringVar()
        self.contents2.set("20")
        self.entrythingy2["textvariable"] = self.contents2
        
        l5 = customtkinter.CTkLabel(leftframe, text="Bonuses", font = ('Z003', 20))
        l5.pack()
        
        self.entrythingyA = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingyA.pack()
        self.contentsA = tk.StringVar()
        self.contentsA.set("0")
        self.entrythingyA["textvariable"] = self.contentsA
                
        l2 = customtkinter.CTkLabel(leftframe, text="Add Number To Damage Total", font = ('Z003', 20))
        l2.pack()
        self.entrythingy3 = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingy3.pack()
        self.contents3 = tk.StringVar()
        self.contents3.set("")
        self.entrythingy3["textvariable"] = self.contents3
 #==============================================================================                          
        l6 = customtkinter.CTkLabel(leftframe, text="Damage Dies\n", font = ('Z003', 20))
        l6.pack()
        
        d4 = customtkinter.CTkLabel(leftframe, text="d4's", font = ('Z003', 20))
        d4.pack()
        self.entrythingyB = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingyB.pack()
        self.contentsB = tk.StringVar()
        self.contentsB.set("0")
        self.entrythingy["textvariable"] = self.contentsB
        
        d6 = customtkinter.CTkLabel(leftframe, text="d6's", font = ('Z003', 20))
        d6.pack()        
        self.entrythingyC = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingyC.pack()
        self.contentsC = tk.StringVar()
        self.contentsC.set("0")
        self.entrythingyC["textvariable"] = self.contentsC
        
        d8 = customtkinter.CTkLabel(leftframe, text="d8's", font = ('Z003', 20))
        d8.pack()
        self.entrythingyD = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingyD.pack()
        self.contentsD = tk.StringVar()
        self.contentsD.set("0")
        self.entrythingy["textvariable"] = self.contentsD
        
        d10 = customtkinter.CTkLabel(leftframe, text="d10's", font = ('Z003', 20))
        d10.pack()        
        self.entrythingyE = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingyE.pack()
        self.contentsE = tk.StringVar()
        self.contentsE.set("0")
        self.entrythingyE["textvariable"] = self.contentsE
        
        d12 = customtkinter.CTkLabel(leftframe, text="d12's", font = ('Z003', 20))
        d12.pack()        
        self.entrythingyF = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingyF.pack()
        self.contentsF = tk.StringVar()
        self.contentsF.set("0")
        self.entrythingyF["textvariable"] = self.contentsF
        
        d20 = customtkinter.CTkLabel(leftframe, text="d20's", font = ('Z003', 20))
        d20.pack()        
        self.entrythingy10 = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingy10.pack()
        self.contents10 = tk.StringVar()
        self.contents10.set("0")
        self.entrythingy10["textvariable"] = self.contents10 
          
        d100 = customtkinter.CTkLabel(leftframe, text="d100's", font = ('Z003', 20))
        d100.pack()        
        self.entrythingy11 = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.entrythingy11.pack()
        self.contents11 = tk.StringVar()
        self.contents11.set("0")
        self.entrythingy11["textvariable"] = self.contents11                  
#==============================================================================                    

        l7 = customtkinter.CTkLabel(leftframe, text="Enemy HP", font = ('Z003', 20))
        l7.pack()         
        self.entrythingy6 = customtkinter.CTkEntry(leftframe, placeholder_text="100", font = ('Z003', 20))
        self.entrythingy6.pack()
        self.contents6 = tk.StringVar()
        self.contents6.set("100")
        self.entrythingy6["textvariable"] = self.contents6  
        
        l4 = customtkinter.CTkLabel(leftframe, text="Enemy Armor Class(AC)", font = ('Z003', 20))
        l4.pack()         
        self.entrythingy7 = customtkinter.CTkEntry(leftframe, placeholder_text="10", font = ('Z003', 20))
        self.entrythingy7.pack()
        self.contents7 = tk.StringVar()
        self.contents7.set("10")
        self.entrythingy7["textvariable"] = self.contents7 
                                       
        c1 = customtkinter.CTkCheckBox(leftframe, text='Lucky',variable=luck, onvalue=True, offvalue=False, command=self.enablelr2s, font = ('Z003', 20))
        c1.pack()
        
        c2 = customtkinter.CTkCheckBox(leftframe, text='Lucky Removes 2\'s',variable=lucktype, onvalue=2, offvalue=1, state='disabled', font = ('Z003', 20))
        c2.pack()  
             
        B = customtkinter.CTkButton(topframe, 
        text = 'Run Simulation',
        command = self.run, 
        font = ('Z003', 25),
        height=70, 
        width=100)
        B.pack()
        output = customtkinter.CTkTextbox(
        bottomframe,
        state='disabled',
        height = 400,
        width = 400
        )  
        output.pack()
        ToolTip(l1, msg="Set the Lowest and Highest number your Hit(roll to hit) die")
        ToolTip(l2, msg="Add an interger to the total of the damage of the die")
        ToolTip(l4, msg="Enemy Armor Class, means you need to roll higher to hurt the enemy")
        ToolTip(l5, msg="Add a modifier(positive) to the roll to hit")
        ToolTip(l6, msg="Select The ammount of each die for one turn's of damage")
        ToolTip(l7, msg="Ammount of Hitpoints the enemy has")
        ToolTip(c1, msg="Enable the Lucky Trait, this one is specifically the halfing lucky racial trait")
        ToolTip(c2, msg="In the lucky trait, make it so not only it rerolls on 1's, but it also rerolls on 2's")
        ToolTip(B, msg="Run The Test Battle To get averages, misses, and rolls to kill")        
    def enablelr2s(self):
        global c2
        if luck.get() == True:
            c2.configure(state='normal')
            c2.update()
        else:
            c2.configure(state='disabled')
            c2.update()
    def setluck(self):
        if luck.get() == True:
            attackroll.luck = True
            attackroll.lucktype = 0
        else:
            attackroll.luck = False
            
    def setlucktype(self):
        if lucktype.get() == 2:
            attackroll.lucktype = 2
        else:
            attackroll.lucktype = 1
    def exit(self):
        sys.exit(0)            
    def run(self):
        mini = self.entrythingy.get()
        maxi = self.entrythingy2.get()
        die2 = self.entrythingyA.get()                
        mods = self.entrythingy3.get() 
        HP = self.entrythingy6.get()
        AC = self.entrythingy7.get()
        
        d4cnt = self.entrythingyB.get() 
        d6cnt = self.entrythingyC.get()  
        d8cnt = self.entrythingyD.get() 
        d10cnt = self.entrythingyE.get()
        d12cnt = self.entrythingyF.get() 
        d20cnt = self.entrythingy10.get()
        d100cnt = self.entrythingy11.get() 
                                    
        attackroll.mini = mini
        attackroll.maxi = maxi
        attackroll.die2 = die2
        attackroll.mods = mods
        attackroll.die = 1
        attackroll.hp = HP
        attackroll.ac = AC
        attackroll.d4 = d4cnt
        attackroll.d6 = d6cnt
        attackroll.d8 = d8cnt
        attackroll.d10 = d10cnt
        attackroll.d12 = d12cnt
        attackroll.d20 = d20cnt
        attackroll.d100 = d100cnt

        self.setluck()
        self.setlucktype()
        attackroll.main()
        output.configure(state='normal')
        output.delete(1.0, END)
        str1 = attackroll.opt
        output.insert(END, str1) 
        output.configure(state='disabled')  
            
if __name__ == "__main__":
    title = "RPG Enemy Tool"
    root = customtkinter.CTk(className = "Rpg Enemy Tool")
    root.geometry('600x1000')
    myapp = App(root)
    myapp.master.title(title)
    myapp.mainloop()
