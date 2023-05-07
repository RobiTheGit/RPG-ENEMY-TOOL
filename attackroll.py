import random
import rpgattackcnt
import re
#This is just doing all of the math for the gui version, please don't run this on it's own, it wont do anything if you do, well acutally it will, but you wouldn't be able to tell
#Basically, it would run the simulation with the deaults, and no output, I have tested it
global opt
opt = ''
def Average(lst):
    return sum(lst) / len(lst)
def main():
    global luck
    global mini
    global maxi
    global mini2
    global maxi2
    global numlist
    global temptnumlist      
    global mods
    global lucktype
    global die
    global die2
    global toroll
    global hp
    global ac
    global hitlist
    global d4
    global d6
    global d8
    global d10
    global d12    
    global d20
    global d100
    global ortherdie
    global numlist2
    global temptnumlist2            
    try:
        die = abs(int(die))
        if die > 100:
            die = 100        
    except:
        die = 1
    try:
        die2 = abs(int(die2))
        if die2 > 100:
            die2 = 100  
        if die2 < 0:
            die2 = 0      
    except:
        die2 = 1        
    try:
        mini = abs(int(mini))
    except:
        mini = 1
    try:
        maxi = abs(int(maxi))
    except:
        maxi = 20
    try:
        mini2 = abs(int(mini2))
    except:
        mini2 = 1
    try:
        maxi2 = abs(int(maxi2))
    except:
        maxi2 = 20
    try:
        mods = abs(int(mods))
    except:
        mods = 0
    try:
        d4 = abs(int(d4))
        if d4 > 100:
            d4 = 100  
        if d4 < 0:
            d4 = 0      
    except:
        d4 = 0 
    try:
        d6 = abs(int(d6))
        if d6 > 100:
            d6 = 100  
        if d6 < 0:
            d6 = 0      
    except:
        d6 = 0
    try:
        d8 = abs(int(d8))
        if d8 > 100:
            d8 = 100  
        if d8 < 0:
            d8 = 0      
    except:
        d8 = 0 
    try:
        d10 = abs(int(d10))
        if d10 > 100:
            d10 = 100  
        if d10 < 0:
            d10 = 0      
    except:
        d10 = 0 
    try:
        d12 = abs(int(d12))
        if d12 > 100:
            d12 = 100  
        if d12 < 0:
            d12 = 0      
    except:
        d12 = 0 
    try:
        d20 = abs(int(d20))
        if d20 > 100:
            d20 = 100  
        if d20 < 0:
            d20 = 0      
    except:
        d20 = 0 
    try:
        d100 = abs(int(d100))
        if d100 > 100:
            d100 = 100  
        if d100 < 0:
            d100 = 0      
    except:
        d100 = 0 
                                        
    numlist = []
    temptnumlist = []     
    temptnumlist2 = []     
    hitlist = [] 
    numlist2 = []
    ortherdie = [] 
    try:
        hp = int(hp)
    except:
        hp = 1000
    global x
    x = 0   
    try:
        ac = int(ac)
    except:
        ac = 10
    ToHit()
def ToHit():
    global luck
    global mini
    global maxi
    global mini2
    global maxi2
    global numlist
    global temptnumlist      
    global mods
    global lucktype
    global die
    global die2
    global toroll
    global hp
    global ac
    global hitlist
    global d4
    global d6
    global d8
    global d10
    global d12    
    global d20
    global d100
    global ortherdie
    global numlist2
    global temptnumlist2                   
    num = random.randint(mini,maxi)
    if num >= ac:
       hitlist.append(1)
       DoMath()
    else:
        if luck == True and maxi == 20:
          if lucktype == 1:
               if num == 1:
                  num = random.randint(mini,maxi)
                  if num >= ac:
                      hitlist.append(1)
                  else:
                      hitlist.append(0)
          if lucktype == 2:
              if num == 1 or num == 2:
                  num = random.randint(mini,maxi)
                  if num >= ac:
                      hitlist.append(1)
                  else:
                      hitlist.append(0)
        else:
            numlist2.append(num)    
            hitlist.append(0)
            temptnumlist2.clear()
            ToHit()
def DoMath():
    global luck
    global mini
    global maxi
    global mini2
    global maxi2
    global numlist
    global temptnumlist      
    global mods
    global lucktype
    global die
    global die2
    global toroll
    global hp
    global ac
    global hitlist
    global d4
    global d6
    global d8
    global d10
    global d12    
    global d20
    global d100
    global ortherdie
    global numlist2
    global temptnumlist2 
    if d4 != 0:
        for y in range(d4):
            num = random.randint(1,4) 
            ortherdie.append(num)   
    if d6 != 0:  
        for y in range(d6):
            num = random.randint(1,6) 
            ortherdie.append(num)           
    if d8 != 0:
        for y in range(d8):
            num = random.randint(1,8)      
            ortherdie.append(num)
    if d10 != 0:
        for y in range(d10):  
            num = random.randint(1,10)    
            ortherdie.append(num)  
    if d12 != 0:
        for y in range(d12):
            num = random.randint(1,12)      
            ortherdie.append(num)
    if d20 != 0:
        for y in range(d20): 
            if luck == True:
                num = random.randint(1,20)     
                if lucktype == 1:
                    if num == 1:
                       num = random.randint(1,20)
                       ortherdie.append(num)
                if lucktype == 2:
                    if num == 1 or num == 2:
                       num = random.randint(1,20)
                       ortherdie.append(num)
                else: 
                    ortherdie.append(num)
            else:
                num = random.randint(1,20)
                ortherdie.append(num)                 
    if d100 != 0:
        for y in range(d100): 
            num = random.randint(1,100)     
            ortherdie.append(num)    
                                                                                                                                                            
    num = sum(ortherdie)
    num += mods
    hp -= num
    numlist.append(num)
    temptnumlist.clear()
    ortherdie.clear()
    if hp > 0:
        try:
            ToHit()
        except:
            BeDone() 
                                                        
    normal = 'Rolls:'
    numbers = f'{numlist}\nAttacked: {len(numlist)}'
    numbers2 = f'{numlist2}\nMissed :{len(numlist2)}'
    numbers3 = len(numlist2) + len(numlist) 
    average = Average(numlist)
    averageoutput = f'Your average hit roll is {re.sub(".0", "", str(round(average, 0)))}'
    hit = int(hitlist.count(1))
    avghit = round(((hit / len(hitlist))*100),2)
    avghitoutput = f"You hit {avghit}% of the time."
    global opt
    opt = f"""
{normal}
Damage When Hit (All Die Together): {numbers}
Numbers That Missed: {numbers2}
{averageoutput}
{avghitoutput}    
Rolls it took to finish the battle: {numbers3}
    """
def BeDone():
    opt = ''
    pass
