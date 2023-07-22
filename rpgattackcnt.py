#!/usr/bin/python3

import random
from tkinter import *
import customtkinter
import tkinter as tk
import attackroll
import sys
import getpass
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
        global SpecialLuckyCheck
        global toroll    
        photo = PhotoImage(file ="dieicon.png")
        root.iconphoto(False, photo)   
        lucktype = tk.IntVar()       
        mods = tk.IntVar()
        luck = tk.IntVar()
        mini = tk.IntVar()
        maxi = tk.IntVar()
        die = tk.IntVar()
#==============================================================================                          
        leftframe = customtkinter.CTkFrame(
        root
        )        
        leftframe.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        leftframe2 = customtkinter.CTkFrame(
        root
        )        
        leftframe2.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1) 
              
        topframe = customtkinter.CTkFrame(
        root 
        )
        topframe.pack(side = TOP, anchor = N, fill=X, expand=1)
                
        bottomframe = customtkinter.CTkFrame(
        root 
        )
        bottomframe.pack(side = BOTTOM, fill=BOTH, pady = 5, expand=1)
        l0 = customtkinter.CTkLabel(topframe, text="RPG Enemy Damage Tool", font = ('Z003', 20))
        l0.pack()
#==============================================================================                                 
        YouStatsLabel = customtkinter.CTkLabel(leftframe, text="Player Stats", font = ('Bold', 20))
        YouStatsLabel.pack()
                                       
        DieLabel = customtkinter.CTkLabel(leftframe, text="Die min and max (To hit)", font = ('Z003', 20))
        DieLabel.pack()
        self.DieMinInput = customtkinter.CTkEntry(leftframe, placeholder_text="1", font = ('Z003', 20))
        self.DieMinInput.pack()
        self.contents = tk.StringVar()
        self.contents.set("1")
        self.DieMinInput["textvariable"] = self.contents
        
        self.DieMaxInput = customtkinter.CTkEntry(leftframe, placeholder_text="20", font = ('Z003', 20))
        self.DieMaxInput.pack()
        self.contents2 = tk.StringVar()
        self.contents2.set("20")
        self.DieMaxInput["textvariable"] = self.contents2
#==============================================================================                                 
        ToHitBonusLabel = customtkinter.CTkLabel(leftframe, text="Bonuses", font = ('Z003', 20))
        ToHitBonusLabel.pack()
        
        self.ToHitBonusInput = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.ToHitBonusInput.pack()
        self.contentsA = tk.StringVar()
        self.contentsA.set("0")
        self.ToHitBonusInput["textvariable"] = self.contentsA
                
        IntBonusLabel = customtkinter.CTkLabel(leftframe, text="Add Number To Damage Total", font = ('Z003', 20))
        IntBonusLabel.pack()
        self.AttackBonusInput = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.AttackBonusInput.pack()
        self.contents3 = tk.StringVar()
        self.contents3.set("")
        self.AttackBonusInput["textvariable"] = self.contents3
#==============================================================================                          
        RollsPerTurnLabel = customtkinter.CTkLabel(leftframe, text="Damage Dies\n", font = ('Z003', 20))
        RollsPerTurnLabel.pack()
        
        d4 = customtkinter.CTkLabel(leftframe, text="d4's", font = ('Z003', 20))
        d4.pack()
        self.D4Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D4Input.pack()
        self.contentsB = tk.StringVar()
        self.contentsB.set("0")
        self.DieMinInput["textvariable"] = self.contentsB
        
        d6 = customtkinter.CTkLabel(leftframe, text="d6's", font = ('Z003', 20))
        d6.pack()        
        self.D6Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D6Input.pack()
        self.contentsC = tk.StringVar()
        self.contentsC.set("0")
        self.D6Input["textvariable"] = self.contentsC
        
        d8 = customtkinter.CTkLabel(leftframe, text="d8's", font = ('Z003', 20))
        d8.pack()
        self.D8Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D8Input.pack()
        self.contentsD = tk.StringVar()
        self.contentsD.set("0")
        self.DieMinInput["textvariable"] = self.contentsD
        
        d10 = customtkinter.CTkLabel(leftframe, text="d10's", font = ('Z003', 20))
        d10.pack()        
        self.D10Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D10Input.pack()
        self.contentsE = tk.StringVar()
        self.contentsE.set("0")
        self.D10Input["textvariable"] = self.contentsE
        
        d12 = customtkinter.CTkLabel(leftframe, text="d12's", font = ('Z003', 20))
        d12.pack()        
        self.D12Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D12Input.pack()
        self.contentsF = tk.StringVar()
        self.contentsF.set("0")
        self.D12Input["textvariable"] = self.contentsF
        
        d20 = customtkinter.CTkLabel(leftframe, text="d20's", font = ('Z003', 20))
        d20.pack()        
        self.D20Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D20Input.pack()
        self.contents10 = tk.StringVar()
        self.contents10.set("0")
        self.D20Input["textvariable"] = self.contents10 
          
        d100 = customtkinter.CTkLabel(leftframe, text="d100's", font = ('Z003', 20))
        d100.pack()        
        self.D100Input = customtkinter.CTkEntry(leftframe, placeholder_text="0", font = ('Z003', 20))
        self.D100Input.pack()
        self.contents11 = tk.StringVar()
        self.contents11.set("0")
        self.D100Input["textvariable"] = self.contents11                  
#==============================================================================                    
        EnemyStatsLabel = customtkinter.CTkLabel(leftframe2, text="Enemy Stats", font = ('Bold', 20))
        EnemyStatsLabel.pack() 
        EnemyHPLabel = customtkinter.CTkLabel(leftframe2, text="Enemy HP", font = ('Z003', 20))
        EnemyHPLabel.pack()         
        self.EnemyHPInput = customtkinter.CTkEntry(leftframe2, placeholder_text="1000", font = ('Z003', 20))
        self.EnemyHPInput.pack()
        self.contents6 = tk.StringVar()
        self.contents6.set("1000")
        self.EnemyHPInput["textvariable"] = self.contents6  
        
        EnemyACLabel = customtkinter.CTkLabel(leftframe2, text="Enemy Armor Class(AC)", font = ('Z003', 20))
        EnemyACLabel.pack()         
        self.EnemyACInput = customtkinter.CTkEntry(leftframe2, placeholder_text="10", font = ('Z003', 20))
        self.EnemyACInput.pack()
        self.contents7 = tk.StringVar()
        self.contents7.set("10")
        self.EnemyACInput["textvariable"] = self.contents7 
 #==============================================================================                                  
        RunButton = customtkinter.CTkButton(topframe, 
        text = 'Run Simulation',
        command = self.run, 
        font = ('Z003', 25),
        height=70, 
        width=100)
        RunButton.pack()
        output = customtkinter.CTkTextbox(
        bottomframe,
        state='disabled',
        height = 400,
        width = 400
        )        
                                         
        LuckyCheck = customtkinter.CTkCheckBox(leftframe, text='Lucky',variable=luck, onvalue=True, offvalue=False, command=self.enablelr2s, font = ('Z003', 20))
        LuckyCheck.pack()
        
        SpecialLuckyCheck = customtkinter.CTkCheckBox(leftframe, text='Lucky Removes 2\'s',variable=lucktype, onvalue=2, offvalue=1, state='disabled', font = ('Z003', 20))
        SpecialLuckyCheck.pack()  
             

        output.pack()
        ToolTip(DieLabel, msg="Set the Lowest and Highest number your Hit(roll to hit) die")
        ToolTip(IntBonusLabel, msg="Add an interger to the total of the damage of the die")
        ToolTip(EnemyACLabel, msg="Enemy Armor Class, means you need to roll higher to hurt the enemy")
        ToolTip(ToHitBonusLabel, msg="Add a modifier(positive) to the roll to hit")
        ToolTip(RollsPerTurnLabel, msg="Select The ammount of each die for one turn's of damage")
        ToolTip(EnemyHPLabel, msg="Ammount of Hitpoints the enemy has")
        ToolTip(EnemyStatsLabel, msg="Enemy Armor Class, HP, etc")
        ToolTip(YouStatsLabel, msg="Player Dies, Bonuses, and Lucky")        
        ToolTip(LuckyCheck, msg="Enable the Lucky Trait, this one is specifically the halfing lucky racial trait")
        ToolTip(SpecialLuckyCheck, msg="In the lucky trait, make it so not only it rerolls on 1's, but it also rerolls on 2's")
        ToolTip(RunButton, msg="Run The Test Battle To get averages, misses, and rolls to kill")        
    def enablelr2s(self):
        global SpecialLuckyCheck
        if luck.get() == True:
            SpecialLuckyCheck.configure(state='normal')
            SpecialLuckyCheck.update()
        else:
            SpecialLuckyCheck.configure(state='disabled')
            SpecialLuckyCheck.update()
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
#Get The Variables
        mini = self.DieMinInput.get()
        maxi = self.DieMaxInput.get()
        die2 = self.ToHitBonusInput.get()                
        mods = self.AttackBonusInput.get() 
        HP = self.EnemyHPInput.get()
        AC = self.EnemyACInput.get()
#All the attack die variables        
        d4cnt = self.D4Input.get() 
        d6cnt = self.D6Input.get()  
        d8cnt = self.D8Input.get() 
        d10cnt = self.D10Input.get()
        d12cnt = self.D12Input.get() 
        d20cnt = self.D20Input.get()
        d100cnt = self.D100Input.get() 
#Put variables in the calculation script                                    
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
        output.configure(state='normal')
        output.delete(1.0, END)
        self.setluck()
        self.setlucktype()
        attackroll.main()
        output.configure(state='normal')
        output.delete(1.0, END)
        str1 = attackroll.opt
        output.insert(END, f"{getpass.getuser().title()} VS Training Dummy")
        output.insert(END, str1) 
        output.configure(state='disabled') 
if __name__ == "__main__":
    title = "RPG Enemy Tool"
    root = customtkinter.CTk(className = "Rpg Enemy Tool")
    root.geometry('1000x1000')
    myapp = App(root)
    myapp.master.title(title)
    myapp.mainloop()
else:
    print("Badonkie donk!\n Run the script by itself please!\n If you are making a tool that encorparates this, you can make it use exec('rpgattackcnt.py') if the tool is in python, or you are using python to run it, or you can delete this text, I won't bite\n\nLoki the dogo says nothing.")
    title = "RPG Enemy Tool"
    root = customtkinter.CTk(className = "Rpg Enemy Tool")
    root.geometry('1000x1000')
    myapp = App(root)
    myapp.master.title(title)
    myapp.mainloop()
