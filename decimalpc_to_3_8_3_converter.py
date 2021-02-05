from tkinter import *


def pc_converter(num):
    
    if num<0:
        return False

     # convert number into binary first 
    binary = bin(num)
     # remove first two characters 
    binary = binary[2:]
    
    
    
    if len(binary)==11:
        # extract last 3 bits 
        startLast3bits= 8
        endLast3bits = 12
        last3bits = binary[startLast3bits : endLast3bits]
        
        # convert extracted last 3bits into decimal again
        decFormOfLast3digits=int(last3bits,2)
        
        #extract middle8bits
        startMiddle8bits= 0
        endMiddle8bits= 8
        middle8bits = binary[startMiddle8bits : endMiddle8bits]
        
        # convert extracted middle 8bits into decimal again
        decFormOfMiddle8digits=int(middle8bits,2)
        
        return '0-%d-%d' %(decFormOfMiddle8digits,decFormOfLast3digits)
        
    elif len(binary)>11 and len(binary)<=14:
        # extract last 3 bits 
        startLast3bits=len(binary)-3
        endLast3bits =len(binary)
        last3bits = binary[startLast3bits : endLast3bits]
        
        # convert extracted last 3bits into decimal again
        decFormOfLast3digits=int(last3bits,2)
        
        #extract middle8bits
        startMiddle8bits=len(binary)-11
        endMiddle8bits=len(binary)-3
        middle8bits = binary[startMiddle8bits : endMiddle8bits]        
      
        # convert extracted middle 8bits into decimal again
        decFormOfMiddle8digits=int(middle8bits,2)
        
        
        #extract first3bits
        startFirst3bits=0
        startFirst8bits=len(binary)-11
        first3bits = binary[startFirst3bits : startFirst8bits]
        
        # convert extracted first 3bits into decimal again
        decFormOfFirst3digits=int(first3bits,2)
        
        return '%d-%d-%d' %(decFormOfFirst3digits,decFormOfMiddle8digits,decFormOfLast3digits)
        
    elif len(binary)<11 and len(binary)>3:  
        # extract last 3 bits 
        startLast3bits=len(binary)-3
        endLast3bits =len(binary)
        last3bits = binary[startLast3bits : endLast3bits]
        
        # convert extracted last 3bits into decimal again
        decFormOfLast3digits=int(last3bits,2)
        
        # extract binary length until last 3 bits 
        startMiddle8bits=0
        endMiddle8bits=len(binary)-3
        middle8bits = binary[startMiddle8bits : endMiddle8bits]
        
        # convert extracted binary length until last 3 bits 
        decFormOfMiddle8digits=int(middle8bits,2)
        
        return '0-%d-%d' %(decFormOfMiddle8digits,decFormOfLast3digits)     
    elif len(binary)<=3:
        # extract last 3 digits only
        startLast3bits=0
        endLast3bits =len(binary)
        last3bits = binary[startLast3bits : endLast3bits]
        
        # convert extracted last 3bits into decimal again
        decFormOfLast3digits=int(last3bits,2)
        
        return '0-0-%d' %(decFormOfLast3digits)
    else:
        return 'You entered invalid Point Code decimal value: %d however it should in the range of 0-16383 according to ITU specification' %(num)

        

master = Tk()
master.title("SS7 Decimal Converter to 3-8-3 Format")

Label(master, text="Decimal Form:").grid(row=0)
Label(master, text="3-8-3 Form:").grid(row=1)

e1 = Entry(master)
e1.grid(row=0, column=1)


Button(master, text='Quit', command=master.quit).grid(row=1, column=0, sticky=E, pady=4)
Button(master, text='Show', command=pc_converter).grid(row=1, column=1, sticky=W, pady=4)
